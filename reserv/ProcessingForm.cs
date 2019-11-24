using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reserv
{
    public partial class ProcessingForm : Form
    {
        CreateForm formData;
        private int downloadingStatus;
        public string NowPluginInstalling;
        private WebClient client;

        public ProcessingForm(CreateForm data)
        {
            this.formData = data;
            InitializeComponent();
            this.Text = "Создание " + formData.nameBox.Text + "...";
            Directory.CreateDirectory("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text);
            DownloadServer(0);
        }
        public void DownloadServer(int status)
        {
            switch (status)
            {
                case 0:
                    using (WebClient client = new WebClient())
                    {
                        client.DownloadProgressChanged += new DownloadProgressChangedEventHandler(client_DownloadProgressChanged);
                        client.DownloadFileCompleted += new AsyncCompletedEventHandler(client_DownloadFileCompleted);
                        downloadingStatus = 0;
                        client.DownloadFileAsync(new Uri("http://api.upbits.org:2488/api/v1/reserv/data/bundle"), @"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/bundle.zip");
                    }
                    break;
                case 1:
                    foreach (dynamic version in formData.cores_request.items)
                    {
                        if (version.name == formData.versionBox.SelectedItem.ToString())
                        {
                            client = new WebClient();
                            client.DownloadProgressChanged += new DownloadProgressChangedEventHandler(client_DownloadProgressChanged);
                            client.DownloadFileCompleted += new AsyncCompletedEventHandler(client_DownloadFileCompleted);
                            downloadingStatus = 1;
                            if (formData.coretypeBox.SelectedItem.ToString() == "Spigot")
                            {
                                client.DownloadFileAsync(new Uri(Convert.ToString(version.downloads.Spigot)), @"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/" + Convert.ToString(version.name) + ".jar");
                            }
                            else if (formData.coretypeBox.SelectedItem.ToString() == "Craftbukkit")
                            {
                                client.DownloadFileAsync(new Uri(Convert.ToString(version.downloads.Craftbukkit)), @"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/" + Convert.ToString(version.name) + ".jar");
                            }
                        }
                    }
                    break;
                case 2:
                    using (WebClient client = new WebClient())
                    {
                        client.DownloadProgressChanged += new DownloadProgressChangedEventHandler(client_DownloadProgressChanged);
                        client.DownloadFileCompleted += new AsyncCompletedEventHandler(client_DownloadFileCompleted);
                        downloadingStatus = 2;
                        if (formData.spawnList.SelectedItem.ToString() == "(стандартный мир)")
                        {
                            client_DownloadFileCompleted(this, new AsyncCompletedEventArgs(null, false, this));
                            break;
                        }

                        foreach (dynamic server in formData.spawns_request.items)
                        {
                            if (server.name == formData.spawnList.SelectedItem.ToString())
                            {
                                // client.DownloadFileAsync(new Uri("http://api.upbits.org:2488/api/v1/reserv/data/bundle"), @"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/bundle.zip");
                                client.DownloadFileAsync(new Uri(Convert.ToString(server.download)), @"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/spawn.zip");
                            }
                        }
                    }
                    break;
            }
        }
        private void cancelButton_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Вы действительно хотите отменить создание сервера?", "Подтверждение", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                client.CancelAsync();
                // installPlugins.CancelAsync();
            }
        }

        void client_DownloadProgressChanged(object sender, DownloadProgressChangedEventArgs e)
        {
            double bytesIn = double.Parse(e.BytesReceived.ToString());
            double totalBytes = double.Parse(e.TotalBytesToReceive.ToString());
            double percentage = bytesIn / totalBytes * 100;

            switch (downloadingStatus)
            {
                case 0:
                    processLabel.Text = "Статус: Загрузка структуры файлов  (" + Math.Round(percentage).ToString() + "%)...";
                    allBar.Value = Convert.ToInt32((double.Parse(Math.Truncate(percentage).ToString()) / 100) * 10);
                    stepLabel.Text = "Шаг 1 из 4";
                    break;
                case 1:
                    processLabel.Text = "Статус: Загрузка ядра (" + Math.Round(percentage).ToString() + "%)...";
                    allBar.Value = Convert.ToInt32(((double.Parse(Math.Truncate(percentage).ToString()) / 100) * 30) + 10);
                    stepLabel.Text = "Шаг 2 из 4";
                    break;
                case 2:
                    processLabel.Text = "Статус: Загрузка спавна (" + Math.Round(percentage).ToString() + "%)...";
                    allBar.Value = Convert.ToInt32(((double.Parse(Math.Truncate(percentage).ToString()) / 100) * 10) + 40);
                    stepLabel.Text = "Шаг 3 из 4";
                    break;
            }
            label1.Text = "Общий процесс: (" + allBar.Value.ToString() + "%)";
            progressBar.Value = int.Parse(Math.Truncate(percentage).ToString());
        }
        void client_DownloadFileCompleted(object sender, AsyncCompletedEventArgs e)
        {
            if (e.Cancelled == false)
            {
                switch (downloadingStatus)
                {
                    case 0:
                        ZipFile.ExtractToDirectory("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/bundle.zip", "C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text);
                        File.Delete(@"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/bundle.zip");
                        string properties = File.ReadAllText("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/server.properties");
                        properties = properties.Replace("spawn-protection=RESERV", "spawn-protection=" + formData.protectionBox.Text);

                        if (formData.netherBox.SelectedItem.ToString() == "Включен")
                            properties = properties.Replace("allow-nether=RESERV", "allow-nether=true");
                        else
                            properties = properties.Replace("allow-nether=RESERV", "allow-nether=false");

                        if (formData.gamemodeBox.SelectedItem.ToString() == "Креатив")
                            properties = properties.Replace("gamemode=RESERV", "gamemode=1");
                        else if (formData.gamemodeBox.SelectedItem.ToString() == "Выживание")
                            properties = properties.Replace("gamemode=RESERV", "gamemode=0");
                        else if (formData.gamemodeBox.SelectedItem.ToString() == "Приключения")
                            properties = properties.Replace("gamemode=RESERV", "gamemode=2");
                        else if (formData.gamemodeBox.SelectedItem.ToString() == "Наблюдатель")
                            properties = properties.Replace("gamemode=RESERV", "gamemode=3");

                        if (formData.queryBox.SelectedItem.ToString() == "Включен")
                            properties = properties.Replace("enable-query=RESERV", "enable-query=true");
                        else if (formData.queryBox.SelectedItem.ToString() == "Выключен")
                            properties = properties.Replace("enable-query=RESERV", "enable-query=false");

                        if (formData.difficultyBox.SelectedItem.ToString() == "Мирная")
                            properties = properties.Replace("difficulty=RESERV", "difficulty=0");
                        else if (formData.difficultyBox.SelectedItem.ToString() == "Легкая")
                            properties = properties.Replace("difficulty=RESERV", "difficulty=1");
                        else if (formData.difficultyBox.SelectedItem.ToString() == "Нормальная")
                            properties = properties.Replace("difficulty=RESERV", "difficulty=2");
                        else if (formData.difficultyBox.SelectedItem.ToString() == "Сложная")
                            properties = properties.Replace("difficulty=RESERV", "difficulty=3");

                        if (formData.monsterBox.SelectedItem.ToString() == "Разрешен")
                            properties = properties.Replace("spawn-monsters=RESERV", "spawn-monsters=true");
                        else if (formData.monsterBox.SelectedItem.ToString() == "Запрещен")
                            properties = properties.Replace("spawn-monsters=RESERV", "spawn-monsters=false");

                        if (formData.pvpBox.SelectedItem.ToString() == "Разрешен")
                            properties = properties.Replace("pvp=RESERV", "pvp=true");
                        else if (formData.pvpBox.SelectedItem.ToString() == "Запрещен")
                            properties = properties.Replace("pvp=RESERV", "pvp=false");

                        if (formData.hardcoreBox.SelectedItem.ToString() == "Включен")
                            properties = properties.Replace("hardcore=RESERV", "hardcore=true");
                        else if (formData.hardcoreBox.SelectedItem.ToString() == "Выключен")
                            properties = properties.Replace("hardcore=RESERV", "hardcore=false");

                        if (formData.commandblocksBox.SelectedItem.ToString() == "Разрешены")
                            properties = properties.Replace("enable-command-block=RESERV", "enable-command-block=true");
                        else if (formData.commandblocksBox.SelectedItem.ToString() == "Запрещены")
                            properties = properties.Replace("enable-command-block=RESERV", "enable-command-block=false");

                        properties = properties.Replace("max-players=RESERV", "max-players=" + formData.maxplayersBox.Text);

                        if (formData.portBox.ToString() != "<auto>")
                            properties = properties.Replace("server-port=RESERV", "server-port=" + formData.portBox.Text);

                        properties = properties.Replace("view-distance=RESERV", "view-distance=" + formData.viewdistanceBox.Text);

                        if (formData.animalsBox.SelectedItem.ToString() == "Разрешено")
                            properties = properties.Replace("spawn-animals=RESERV", "spawn-animals=true");
                        else if (formData.animalsBox.SelectedItem.ToString() == "Запрещено")
                            properties = properties.Replace("spawn-animals=RESERV", "spawn-animals=false");

                        if (formData.structureBox.SelectedItem.ToString() == "Разрешено")
                            properties = properties.Replace("generate-structures=RESERV", "generate-structures=true");
                        else if (formData.structureBox.SelectedItem.ToString() == "Запрещено")
                            properties = properties.Replace("generate-structures=RESERV", "generate-structures=false");

                        properties = properties.Replace("motd=RESERV", "motd=" + formData.nameBox.Text);
                        properties = properties.Replace("filename-type=RESERV", "filename-type=" + formData.versionBox.SelectedItem.ToString());

                        File.WriteAllText("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/server.properties", properties);

                        if (formData.serverPicture.ImageLocation.ToString().StartsWith("http") == true)
                        {
                            using (WebClient wb = new WebClient())
                            {
                                byte[] imageData = wb.DownloadData(new Uri(formData.serverPicture.ImageLocation)); //DownloadData function from here
                                MemoryStream stream = new MemoryStream(imageData);

                                new Bitmap(Image.FromStream(stream), new Size(64, 64)).Save("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/server-icon.png", ImageFormat.Png);

                                stream.Close();
                            }
                        }
                        else
                        {
                            new Bitmap(Image.FromFile(formData.serverPicture.ImageLocation), new Size(64, 64)).Save("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/server-icon.png", ImageFormat.Png);
                        }
                        DownloadServer(1);
                        break;
                    case 1:
                        DownloadServer(2);
                        break;
                    case 2:
                        if (formData.spawnList.SelectedItem.ToString() != "(стандартный мир)")
                        {
                            ZipFile.ExtractToDirectory("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/spawn.zip", "C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text);
                            File.Delete(@"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/spawn.zip");
                        }
                        cancelButton.Enabled = false;
                        installPlugins.RunWorkerAsync();
                        break;
                }
            }
            else
            {
                Directory.Delete("C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text, true);
                this.Close();
            }

        }
        private void installPlugins_DoWork(object sender, DoWorkEventArgs e)
        {
            if (formData.PluginsToInstall.Count != 0)
            {
                int procentCount = (50 / formData.PluginsToInstall.Count);
                int procents = 0;
                dynamic list;
                if (Properties.Settings.Default.SpiGetEnabled == true)
                {
                    list = formData.plugins_request;
                }
                else
                {
                    list = formData.plugins_request.items;
                }
                foreach (string plugin in formData.PluginsToInstall)
                {
                    foreach (dynamic plugindata in list)
                    {
                        if (plugin == Convert.ToString(plugindata.name))
                        {
                            procents += procentCount;
                            installPlugins.ReportProgress(procents);
                            string downloadURL;
                            using (WebClient client = new WebClient())
                            {
                                if (Properties.Settings.Default.SpiGetEnabled == true)
                                {
                                    downloadURL = "https://api.spiget.org/v2/resources/" + Convert.ToString(plugindata.id) + "/download";
                                }
                                else
                                {
                                    downloadURL = Convert.ToString(plugindata.download);
                                }
                                try
                                {
                                    client.DownloadFile(new Uri(downloadURL), @"C:/Users/" + Environment.UserName + "/Documents/Reserv/" + formData.nameBox.Text + "/plugins/" + Convert.ToString(plugindata.name) + ".jar");
                                }
                                catch (System.Net.WebException)
                                {
                                    MessageBox.Show("Во время загрузки " + plugindata.name + " произошла ошибка загрузки. В избежании проблем мы вынуждены пропустить установку этого плагина.", "Ошибка установки " + plugindata.name, MessageBoxButtons.OK, MessageBoxIcon.Error);
                                    continue;
                                }

                            }
                            break;
                        }
                    }
                }
            }

        }

        private void installPlugins_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (e.Cancelled == false)
            {
                processLabel.Text = "Статус: Установка плагинов (100%)...";
                allBar.Value = 100;
                this.Hide();
                new CreatedForm(formData.nameBox.Text.ToString(), formData.versionBox.SelectedItem.ToString(), formData.maxplayersBox.Text.ToString(), formData.PluginsToInstall.Count.ToString()).ShowDialog();
                this.Close();
            }

        }

        private void installPlugins_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            progressBar.Value = e.ProgressPercentage * 2;
            stepLabel.Text = "Шаг 4 из 4";
            processLabel.Text = "Статус: Установка плагинов (" + (e.ProgressPercentage * 2).ToString() + "%)...";
            label1.Text = "Общий процесс: (" + allBar.Value.ToString() + "%)";
            allBar.Value = 50 + e.ProgressPercentage;
        }
    }
 }
