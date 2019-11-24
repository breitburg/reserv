using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using xNet;
using System.Threading;
using Newtonsoft.Json.Linq;

namespace Reserv
{
    public partial class ListForm : Form
    {
        public Process p = new Process();
        public List<string> PlayersOnline = new List<string>();
        private string CurrentServerDirectory;
        private Dictionary<string, string> data = new Dictionary<string, string>();

        public ListForm()
        {
            InitializeComponent();
            выводитьУведомленияToolStripMenuItem.Checked = Properties.Settings.Default.NotificationsAllowed;
            использоватьБазуToolStripMenuItem.Checked = Properties.Settings.Default.SpiGetEnabled;

            if (Directory.Exists("C:/Users/" + Environment.UserName + "/Documents/Reserv") == false)
            {
                Directory.CreateDirectory("C:/Users/" + Environment.UserName + "/Documents/Reserv");
            } else {
                foreach (string ServerName in Directory.GetDirectories("C:/Users/" + Environment.UserName + "/Documents/Reserv"))
                {
                    serverList.Items.Add(ServerName.Split('\\').Last());
                }
            }
            if (serverList.Items.Count != 0)
                serverList.SelectedIndex = 0;
            if (Properties.Settings.Default.ExperimentalEnabled == true)
                экспериментальныеФункцииToolStripMenuItem.Enabled = false;
            else
            {
                экспериментальноToolStripMenuItem.Visible = false;
            }
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            CreateForm createForm = new CreateForm();
            createForm.ShowDialog();
            serverList.Items.Clear();
            foreach (string ServerName in Directory.GetDirectories("C:/Users/" + Environment.UserName + "/Documents/Reserv"))
            {
                serverList.Items.Add(ServerName.Split('\\').Last());
            }
            if (serverList.Items.Count == 0)
                deleteButton.Enabled = false;
            else
                serverList.SelectedIndex = 0;
            GC.Collect();
            GC.WaitForPendingFinalizers();
        }

        private void serverList_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (serverList.SelectedItem != null)
            {
                splitContainer.Panel2.Enabled = true;
                CurrentServerDirectory = "C:/Users/" + Environment.UserName + "/Documents/Reserv/" + serverList.SelectedItem;
                pictureBox1.ImageLocation = CurrentServerDirectory + "/server-icon.png";
                tabControl.Enabled = true;

                data = new Dictionary<string, string>();
                if (File.Exists(CurrentServerDirectory + "/server.properties") == true)
                {
                    foreach (var row in File.ReadAllLines(CurrentServerDirectory + "/server.properties"))
                        if ((row.Split('=')[0].StartsWith("#") == false) && (row.Split('=')[0] != ""))
                            data.Add(row.Split('=')[0], string.Join("=", row.Split('=').Skip(1).ToArray()));

                    serverName.Text = data["motd"];
                    serverPlayers.Text = data["max-players"];
                    serverPort.Text = data["server-port"];
                    if (data["difficulty"] == "0")
                        serverDifficulty.Text = "Мирная";
                    else if (data["difficulty"] == "1")
                        serverDifficulty.Text = "Легкая";
                    else if (data["difficulty"] == "2")
                        serverDifficulty.Text = "Нормальная";
                    else if (data["difficulty"] == "3")
                        serverDifficulty.Text = "Сложная";
                    else
                        serverDifficulty.Text = "Неизвестно";

                    if (data["enable-command-block"] == "true")
                        serverCB.Text = "Включены";
                    else if (data["enable-command-block"] == "false")
                        serverCB.Text = "Выключены";
                    else
                        serverDifficulty.Text = "Неизвестно";

                    if (data["pvp"] == "true")
                        serverPVP.Text = "Включено";
                    else if (data["pvp"] == "false")
                        serverPVP.Text = "Выключено";
                    else
                        serverDifficulty.Text = "Неизвестно";

                    if (data["online-mode"] == "true")
                        serverLicense.Text = "Лицензия";
                    else if (data["online-mode"] == "false")
                        serverLicense.Text = "Пиратка";
                    else
                        serverDifficulty.Text = "Неизвестно";

                    deleteButton.Enabled = true;
                }
                else
                {
                    MessageBox.Show("При попытке получения данных о сервере произошла ошибка. Скорее всего эта ошибка вызвана ошибкой при удалении сервера.", "Ошибка получения данных", MessageBoxButtons.OK, MessageBoxIcon.Warning);

                    while (true) {
                        try
                        {
                            Directory.Delete(CurrentServerDirectory, true);
                            break;
                        }
                        finally { }
                        
                    }
                    
                    serverList.Items.Remove(serverList.SelectedItem);
                }
            }
            else
                deleteButton.Enabled = false;
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            DialogResult deleteResult = MessageBox.Show("Вы действительно хотите удалить " + serverList.SelectedItem.ToString() + "?\nПосле удаления вы не сможете восстановить файлы сервера.", "Удаление " + serverList.SelectedItem.ToString(), MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2);
            if (deleteResult == DialogResult.Yes)
            {
                try
                {
                    Directory.Delete(CurrentServerDirectory, true);
                    splitContainer.Panel2.Enabled = false;
                    serverList.Items.Remove(serverList.SelectedItem.ToString());
                }
                catch (System.IO.IOException)
                {
                    MessageBox.Show("При удалении сервера возникла ошибка. Скорее всего это связано с тем, что процесс сервера не остановлен. Попробуйте перезапустить программу и повторить попытку.", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    Environment.Exit(0);
                }
                
            }
        }

        private void runningServer_DoWork(object sender, DoWorkEventArgs e)
        {
            // string current_dir;
            Environment.CurrentDirectory = CurrentServerDirectory;
            p.StartInfo.FileName = "java";
            p.StartInfo.Arguments = @"-Xmx1024M -Xms1024M -jar " + '"' + CurrentServerDirectory + "/" + data["filename-type"] + ".jar" + '"' + " nogui";
            p.StartInfo.UseShellExecute = false;  // ShellExecute = true not allowed when output is redirected..
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            // p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            try
            {
                p.Start();
                ShowNotification("Запуск сервера...", ToolTipIcon.Info);
                StreamReader sr = p.StandardOutput;
                while (!sr.EndOfStream)
                {
                    String s = sr.ReadLine();
                    MethodInvoker inv = delegate
                    {
                        Encoding srcEnc = p.StandardOutput.CurrentEncoding;
                        byte[] bSrc = srcEnc.GetBytes(s);

                        Encoding unicodeEnc = Encoding.Unicode;
                        byte[] resArr = Encoding.Convert(Encoding.GetEncoding(866), unicodeEnc, bSrc);

                        if (unicodeEnc.GetString(resArr).Contains("For help, type " + '"' + "help" + '"' + " or " + '"' + "?" + '"') || unicodeEnc.GetString(resArr).Contains("For help, type " + '"' + "help" + '"') == true)
                        {
                            stopButton.Enabled = true;
                            commandBox.Enabled = true;
                            ShowNotification("Сервер успешно запущен.", ToolTipIcon.Info);
                        }
                        else if (unicodeEnc.GetString(resArr).Contains("Address already in use: bind") == true)
                        {
                            if (MessageBox.Show("Указанный порт занят другим процессом, это припятствует запуску вашего сервера. Завершить процесс принудительно?", "Ошибка запуска", MessageBoxButtons.YesNo, MessageBoxIcon.Error, MessageBoxDefaultButton.Button2) == DialogResult.Yes)
                            {
                                foreach (Process proc in Process.GetProcessesByName("java"))
                                {
                                    proc.Kill();
                                }
                                // runServerButton_Click(this, EventArgs.Empty);
                            }
                        }
                        else if (unicodeEnc.GetString(resArr).Contains("Can't keep up! Is the server overloaded?") == true)
                        {
                            ShowNotification("Сервер сообщил о рассинхроне. Возможно такое поведение вызвано в результате перегрузки. Постарайтесь снизить нагрузку на сервер.", ToolTipIcon.Warning);
                        }
                        else if (unicodeEnc.GetString(resArr).Contains("left the game") == true)
                        {
                            ShowNotification("Игрок " + unicodeEnc.GetString(resArr).Split(' ')[2] + " вышел.", ToolTipIcon.Info);
                            PlayersOnline.Remove(unicodeEnc.GetString(resArr).Split(' ')[2]);

                            string LastPlayer = String.Empty;
                            if (PlayersOnline.Count > 0)
                            {
                                if (playersList.SelectedItem != null)
                                {
                                    LastPlayer = playersList.SelectedItem.ToString();
                                    if (playersList.SelectedItem.ToString() == unicodeEnc.GetString(resArr).Split(' ')[2])
                                    {
                                        playersList.SelectedIndex = 0;
                                    }
                                }
                                playersList.Items.Clear();
                                foreach (string playerNickname in PlayersOnline)
                                {
                                    playersList.Items.Add(playerNickname);
                                }
                                if (LastPlayer != String.Empty)
                                {
                                    playersList.SelectedItem = LastPlayer;
                                }
                            }
                            else
                            {
                                playersList.Items.Clear();
                                playersContainer.Panel2.Enabled = false;
                                playerLabel.Text = "<игрок не выбран>";
                                playerHeadIcon.Image = null;
                            }
                            if (PlayersOnline.Count == 1)
                            {
                                playersList.SelectedIndex = 0;
                            }

                        }
                        else if (unicodeEnc.GetString(resArr).Contains("logged in with entity id") == true)
                        {
                            string playerName = unicodeEnc.GetString(resArr).Split(' ')[2].Split('[')[0];
                            ShowNotification("Игрок " + playerName + " зашел.", ToolTipIcon.Info);
                            PlayersOnline.Add(playerName);

                            string LastPlayer = String.Empty;
                            if (PlayersOnline.Count > 0)
                            {
                                if (playersList.SelectedItem != null)
                                {
                                    LastPlayer = playersList.SelectedItem.ToString();
                                }
                                playersList.Items.Clear();
                                foreach (string playerNickname in PlayersOnline)
                                {
                                    playersList.Items.Add(playerNickname);
                                }
                                if (PlayersOnline.Count == 1)
                                {
                                    playersList.SelectedIndex = 0;
                                }
                                else if (LastPlayer != String.Empty)
                                {
                                    playersList.SelectedItem = LastPlayer;
                                }
                            }
                            else
                            {
                                playersContainer.Panel2.Enabled = false;
                                playerHeadIcon.Image = null;
                            }
                        }

                        this.consoleBox.Text += unicodeEnc.GetString(resArr) + Environment.NewLine;
                        consoleBox.SelectionStart = consoleBox.Text.Length;
                        consoleBox.ScrollToCaret();
                    };

                    try
                    {
                        this.Invoke(inv);
                    }
                    finally { }
                }
            }
            catch (System.ComponentModel.Win32Exception)
            {
                if (MessageBox.Show("Извините, для запуска сервера требуется установить Java.\nПерейти на сайт для загрузки?", "Ошибка запуска", MessageBoxButtons.YesNo, MessageBoxIcon.Error, MessageBoxDefaultButton.Button2) == DialogResult.Yes)
                    Process.Start("https://www.java.com/en/download/");
            }
        }

        private void runningServer_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            p.Close();
            runServerButton.Enabled = true;
            stopButton.Enabled = false;
            // consoleBox.Clear();
            commandBox.Clear();
            commandBox.Enabled = false;
            // serverList.Enabled = true;
            splitContainer.Panel1.Enabled = true;
        }

        private void runServerButton_Click(object sender, EventArgs e)
        {
            consoleBox.Clear();
            splitContainer.Panel1.Enabled = false;
            // serverList.Enabled = false;
            runningServer.RunWorkerAsync();
            runServerButton.Enabled = false;
            // commandBox.Enabled = true;
        }

        private void stopButton_Click(object sender, EventArgs e)
        {
            playersList.Items.Clear();
            playersContainer.Panel2.Enabled = false;
            p.StandardInput.WriteLine("stop");
            stopButton.Enabled = false;
            ShowNotification("Выключение сервера...", ToolTipIcon.Info);
        }

        private void commandBox_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                byte[] buffer = Encoding.UTF8.GetBytes(commandBox.Text);
                p.StandardInput.BaseStream.Write(buffer, 0, buffer.Length);
                p.StandardInput.WriteLine();
                commandBox.Clear();
            }
        }

        private void оПрограммеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AboutForm about = new AboutForm();
            about.ShowDialog();
        }

        private void поддержатьРазработчиковToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Process.Start("http://www.donationalerts.ru/r/upbits");
        }

        private void сообщитьОбОшибкеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Process.Start("https://vk.com/im?sel=-158101309");
        }

        private void отчиститьКонсольToolStripMenuItem_Click(object sender, EventArgs e)
        {
            consoleBox.Clear();
        }

        private void notifyServer_BalloonTipClicked(object sender, EventArgs e)
        {
            this.Activate();
        }

        private void сохранитьВФайлToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (saveConsoleDialog.ShowDialog() != DialogResult.Cancel)
            {
                File.WriteAllText(saveConsoleDialog.FileName, consoleBox.Text);
                saveConsoleDialog.FileName = String.Empty;
            }
        }

        private void playersList_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (playersList.SelectedItem != null)
            {
                playerHeadIcon.ImageLocation = "https://minotar.net/avatar/" + playersList.SelectedItem.ToString() + "/46.png";
                playerLabel.Text = playersList.SelectedItem.ToString();
                playersContainer.Panel2.Enabled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            BanKickForm ban = new BanKickForm();
            ban.Text = "Забанить " + playersList.SelectedItem.ToString();
            ban.ShowDialog();
            if (ban.isClicked == true)
            {
                byte[] buffer = Encoding.UTF8.GetBytes("ban " + playersList.SelectedItem.ToString() + " " + ban.textBox1.Text.ToString());
                p.StandardInput.BaseStream.Write(buffer, 0, buffer.Length);
                p.StandardInput.WriteLine();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            BanKickForm ban = new BanKickForm();
            ban.Text = "Кикнуть " + playersList.SelectedItem.ToString();
            ban.ShowDialog();
            if (ban.isClicked == true)
            {
                byte[] buffer = Encoding.UTF8.GetBytes("kick " + playersList.SelectedItem.ToString() + " " + ban.textBox1.Text.ToString());
                p.StandardInput.BaseStream.Write(buffer, 0, buffer.Length);
                p.StandardInput.WriteLine();
            }
        }

        private void посмотретьIPToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new IPShowForm().Show();
        }
        
        public void CheckUpdates(bool isOnStart = false)
        {
            new Thread(() => {
                using (var request = new HttpRequest())
                {
                    dynamic versions_request = JObject.Parse(request.Get("http://95.183.8.193:2488/api/v1/reserv/data/versions").ToString());
                    if (versions_request.lastest.release.version != Application.ProductVersion)
                        new UpdateAvailable((versions_request.lastest.release.changelog).ToString(), (versions_request.lastest.release.version).ToString(), (versions_request.lastest.release.download).ToString()).ShowDialog();
                    else
                        if (isOnStart == false)
                            MessageBox.Show("Обновлений не найдено.\nВаша версия является новейшей.", "Обновления не найдены");
                }
            }).Start();
        }

        private void проверитьНаличиеОбновленийToolStripMenuItem_Click(object sender, EventArgs e)
        {
            CheckUpdates();
        }

        private void reservRemoteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new CodeView().ShowDialog();
        }

        private void открытьПапкуССерверамиToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Process.Start("explorer.exe", "/open, C:\\Users\\" + Environment.UserName + "\\Documents\\Reserv\\");
        }

        private void ShowNotification(string body, ToolTipIcon icon)
        {
            if (Properties.Settings.Default.NotificationsAllowed == true)
                notifyServer.ShowBalloonTip(1, "Сервер " + serverName.Text, body, icon);
        }

        private void выводитьУведомленияToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.NotificationsAllowed = выводитьУведомленияToolStripMenuItem.Checked;
            Properties.Settings.Default.Save();
        }

        private void сброситьДанныеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (serverList.Enabled == true)
            {
                if (MessageBox.Show("Вы действительно хотите сбросить все данные и параметры?", "Подтверждение", MessageBoxButtons.YesNo) == DialogResult.Yes)
                {
                    Directory.Delete("C:\\Users\\" + Environment.UserName + "\\Documents\\Reserv\\", true);
                    Properties.Settings.Default.Reset();
                    Properties.Settings.Default.Save();
                    MessageBox.Show("Данные успешно удалены. Перезапустите программу.", "Успешное удаление", MessageBoxButtons.OK);
                    Environment.Exit(0);
                }
            }
        }

        private void отправитьЗапросНаДобавлениеПлагинаToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new UploadPluginForm().ShowDialog();
        }

        private void экспериментальныеФункцииToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.ExperimentalEnabled = true;
            Properties.Settings.Default.Save();
            MessageBox.Show("Экспериментальные возможности активированы. Перезагрузите программу.", "Экспериментальные возможности", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            Environment.Exit(0);
        }

        private void отключитьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.ExperimentalEnabled = false;
            Properties.Settings.Default.Save();
            MessageBox.Show("Экспериментальные возможности были деактивированы. Перезагрузите программу.", "Экспериментальные возможности", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            Environment.Exit(0);
        }

        private void reservRemoteToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            new CodeView().ShowDialog();
        }

        private void автоматизированныеТестыToolStripMenuItem_Click(object sender, EventArgs e)
        {
            new AutomaticTestsForm().ShowDialog();
        }

        private void перейтиНаФорумToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Process.Start("http://upbits.org/forum/");
        }

        private void использоватьБазуToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.SpiGetEnabled = использоватьБазуToolStripMenuItem.Checked;
            Properties.Settings.Default.Save();
            if (использоватьБазуToolStripMenuItem.Checked == true)
            {
                MessageBox.Show("Использование базы данных SpiGet нестабильно, и находится на тестировании. Также, вы теряете возможность выбрать ядро Craftbukkit, только Spigot. При возникновении ошибок сообщите об возникших проблемах на форуме.", "База данных SpiGet");
            }
        }
    }
}
