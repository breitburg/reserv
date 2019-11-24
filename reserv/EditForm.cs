using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Threading;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using xNet;
using System.Diagnostics;

namespace Reserv
{
    public partial class CreateForm : Form
    {
        public dynamic cores_request;
        public dynamic plugins_request;
        public dynamic spawns_request;
        public List<string> PluginsToInstall = new List<string>();
        public CreateForm()
        {
            InitializeComponent();
            difficultyBox.SelectedIndex = 2;
            pvpBox.SelectedIndex = 0;
            hardcoreBox.SelectedIndex = 1;
            gamemodeBox.SelectedIndex = 1;
            monsterBox.SelectedIndex = 0;
            structureBox.SelectedIndex = 0;
            commandblocksBox.SelectedIndex = 1;
            queryBox.SelectedIndex = 1;
            netherBox.SelectedIndex = 0;
            animalsBox.SelectedIndex = 0;
            serverPicture.ImageLocation = "https://image.ibb.co/kdes6z/tvoya_mamka.png";

            foreach (string serverName in Directory.GetDirectories("C:/Users/" + Environment.UserName + "/Documents/Reserv"))
            {   
                if (serverName.Split('\\').Last() == nameBox.Text == true)
                {
                    if (statusLabel.Text == "Сервер готов к сборке...")
                    {
                        statusLabel.Text = "Ошибка: Данное имя сервера уже существует!";
                        statusLabel.ForeColor = Color.Red;
                        nextButton.Enabled = false;
                        break;
                    }
                }
            }
            new Thread(() => {
                using (var request = new HttpRequest())
                {
                    cores_request = JObject.Parse(request.Get("http://api.upbits.org:2488/api/v1/reserv/data/cores").ToString());
                    // MessageBox.Show(String.Join(", ", cores_request.list));
                    foreach (string coreType in cores_request.list)
                    {
                        coretypeBox.Items.Add(coreType);
                    }
                    coretypeBox.SelectedIndex = 0;

                    foreach (dynamic mineVersion in cores_request.items)
                    {
                        versionBox.Items.Add(mineVersion.name);
                    }
                    versionBox.SelectedIndex = 0;

                    if (Properties.Settings.Default.SpiGetEnabled == false)
                    {
                        plugins_request = JObject.Parse(request.Get("http://api.upbits.org:2488/api/v1/reserv/data/plugins").ToString());
                        foreach (dynamic plugin in plugins_request.items)
                        {
                            pluginsBox.Items.Add(plugin.name);
                        }
                        pluginsBox.SelectedIndex = 0;
                    }
                    else
                    {
                        LoadPluginsList();
                    }
                    spawns_request = JObject.Parse(request.Get("http://api.upbits.org:2488/api/v1/reserv/data/spawns").ToString());
                    foreach (dynamic spawn in spawns_request.items)
                    {
                        spawnList.Items.Add(spawn.name);
                    }
                    spawnList.SelectedIndex = 0;
                }
                try {
                    Invoke((Action)(() => { tabControl1.Visible = true; nextButton.Enabled = true; statusLabel.Visible = true;  }));
                }
                finally { }
                
            }).Start();
            pluginsContainer.Panel1Collapsed = !Properties.Settings.Default.SpiGetEnabled;
            coretypeBox.Enabled = !Properties.Settings.Default.SpiGetEnabled;

        }
        private void pluginsBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (PluginsToInstall.Contains(pluginsBox.SelectedItem.ToString()) == true)
            {
                installingLabel.Visible = true;
                installButton.Text = "Удалить";
            }
            else
            {
                installingLabel.Visible = false;
                installButton.Text = "Установить";
            }
            pluginName.Text = pluginsBox.SelectedItem.ToString();
            if (Properties.Settings.Default.SpiGetEnabled == false)
            {
                foreach (dynamic pluginInfo in plugins_request.items)
                {
                    if (pluginInfo.name == pluginsBox.SelectedItem.ToString())
                    {
                        pluginDescription.Text = pluginInfo.description;
                        pluginAuthors.Text = pluginInfo.authors;
                        pluginPicture.ImageLocation = pluginInfo.picture;
                    }
                }
            }
            else
            {
                foreach (dynamic pluginInfo in plugins_request)
                {
                    if (pluginInfo.name == pluginsBox.SelectedItem.ToString())
                    {
                        pluginDescription.Text = pluginInfo.tag;
                        pluginAuthors.Text = Convert.ToString(pluginInfo.downloads) + " загрузок";
                        pluginPicture.ImageLocation = "http://www.spigotmc.org/" + Convert.ToString(pluginInfo.icon.url);
                    }
                }
            }
        }

        private void LoadPluginsList()
        {
            using (var request = new HttpRequest())
            {
                plugins_request = JArray.Parse(request.Get("https://api.spiget.org/v2/resources/new?size=1000&fields=name%2Ctag%2Cicon%2Cdownloads").ToString());
                foreach (dynamic plugin in plugins_request)
                {
                    pluginsBox.Items.Add(plugin.name);
                }
                pluginsBox.SelectedIndex = 0;
            }
        }
        private void customCoreBox_CheckedChanged(object sender, EventArgs e)
        {
            versionBox.Enabled = true;
            coretypeBox.Enabled = true;
            coreDescription.Enabled = true;
            versioLabel.Text = versionBox.SelectedItem.ToString();
            if (coretypeBox.SelectedItem.ToString() == "Craftbukkit")
            {
                corePictuireBox.ImageLocation = cores_request.icons.Craftbukkit;
            }
            else if (coretypeBox.SelectedItem.ToString() == "Spigot")
            {
                corePictuireBox.ImageLocation = cores_request.icons.Spigot;
            }
            foreach (dynamic mineVersion in cores_request.items)
            {
                if (mineVersion.name == versionBox.SelectedItem.ToString())
                {
                    if (mineVersion.allow_plugins == "False")
                    {
                        splitContainer.Enabled = false;
                        splitContainer.Size = new Size(656, 314);
                        warningLabel.Text = "Выбранная вами версия не поддерживает установку плагинов.";
                    }
                    else
                    {
                        splitContainer.Size = new Size(656, 349);
                    }
                }
            }
        }

        private void versionBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            versioLabel.Text = versionBox.SelectedItem.ToString();
            foreach (dynamic mineVersion in cores_request.items)
            {
                if (mineVersion.name == versionBox.SelectedItem.ToString())
                {
                    if (mineVersion.allow_plugins == "False")
                    {
                        splitContainer.Enabled = false;
                        splitContainer.Size = new Size(656, 314);
                        warningLabel.Text = "Выбранная вами версия не поддерживает установку плагинов.";
                    }
                    else
                    {
                        splitContainer.Enabled = true;
                        splitContainer.Size = new Size(656, 349);
                    }
                }
            }
        }

        private void coretypeBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (coretypeBox.SelectedItem.ToString() == "Craftbukkit")
            {
                coreDescription.Text = cores_request.descriptions.Craftbukkit;
                corePictuireBox.ImageLocation = cores_request.icons.Craftbukkit;
            }
            else if (coretypeBox.SelectedItem.ToString() == "Spigot")
            {
                coreDescription.Text = cores_request.descriptions.Spigot;
                corePictuireBox.ImageLocation = cores_request.icons.Spigot;
            }
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            if (MessageBox.Show("Вы действительно хотите возвратить параметры по-умолчанию?", "Настройки по-умолчанию", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2) == DialogResult.Yes)
            {
                difficultyBox.SelectedIndex = 2;
                pvpBox.SelectedIndex = 0;
                hardcoreBox.SelectedIndex = 1;
                gamemodeBox.SelectedIndex = 1;
                monsterBox.SelectedIndex = 0;
                structureBox.SelectedIndex = 0;
                commandblocksBox.SelectedIndex = 1;
                queryBox.SelectedIndex = 1;
                netherBox.SelectedIndex = 0;
                animalsBox.SelectedIndex = 0;
                versionBox.SelectedIndex = 0;
                coretypeBox.SelectedIndex = 0;
                pluginsBox.SelectedIndex = 0;
            }
        }

        private void installButton_Click(object sender, EventArgs e)
        {
            if (PluginsToInstall.Contains(pluginsBox.SelectedItem.ToString()) == false)
            {
                PluginsToInstall.Add(pluginsBox.SelectedItem.ToString());
                installingLabel.Visible = true;
                installButton.Text = "Удалить";
            }
            else
            {
                PluginsToInstall.Remove(pluginsBox.SelectedItem.ToString());
                installingLabel.Visible = false;
                installButton.Text = "Установить";
            }            
        }

        private void createButton_Click(object sender, EventArgs e)
        {
            this.Hide();
            new ProcessingForm(this).ShowDialog();
        }

        private void CreateForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            GC.Collect();
            GC.WaitForPendingFinalizers();
        }

        private void nameBox_TextChanged(object sender, EventArgs e)
        {
            if (nameBox.Text == String.Empty)
            {
                statusLabel.Text = "Ошибка: Название сервера содержит пустую строку!";
                statusLabel.ForeColor = Color.Red;
                nextButton.Enabled = false;
            }
            else if ("А а Б б В в Г г Д д Е е Ё ё Ж ж З з И и Й й К к Л л М м Н н О о П п Р р С с Т т У у Ф ф Х х Ц ц Ч ч Ш ш Щ щ Ъ ъ Ы ы Ь ь Э э Ю ю Я я".Split(' ').Any(x => nameBox.Text.Contains(x))) {
                statusLabel.Text = "Ошибка: Название сервера содержит русские символы!";
                statusLabel.ForeColor = Color.Red;
                nextButton.Enabled = false;
            }
            else if (nameBox.Text != String.Empty)
            {
                statusLabel.Text = "Сервер готов к сборке...";
                statusLabel.ForeColor = Color.DarkOliveGreen;
                nextButton.Enabled = true;
                foreach (string serverName in Directory.GetDirectories("C:/Users/" + Environment.UserName + "/Documents/Reserv"))
                {
                    if (serverName.Split('\\').Last() == nameBox.Text == true)
                    {
                        statusLabel.Text = "Ошибка: Данное имя сервера уже существует!";
                        statusLabel.ForeColor = Color.Red;
                        nextButton.Enabled = false;
                        break;
                    }
                }
            }
        }

        private void spawnList_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (spawnList.SelectedItem.ToString() == "(стандартный мир)")
            {
                spawnLabel.Text = "Обычный мир";
                spawnPicture.ImageLocation = "http://minecraft.tools/en/img/presets/normal.jpg";
                spawnDescription.Text = "Стандартный мир Minecraft, котрый создается при создании нового мира.";
            }
            else
            {
                foreach (dynamic spawn in spawns_request.items)
                {
                    if (spawn.name == spawnList.SelectedItem.ToString())
                    {
                        spawnLabel.Text = spawn.name;
                        spawnPicture.ImageLocation = spawn.picture;
                        spawnDescription.Text = spawn.description;
                        break;
                    }
                }
            }
        }

        private void openPictureButton_Click(object sender, EventArgs e)
        {
            if (openPictureDialog.ShowDialog() == DialogResult.OK)
                serverPicture.ImageLocation = openPictureDialog.FileName;
        }

        private void cancelPictureButton_Click(object sender, EventArgs e)
        {
            serverPicture.ImageLocation = "https://image.ibb.co/kdes6z/tvoya_mamka.png";
        }

        private void searchBox_TextChanged(object sender, EventArgs e)
        {
            if (searchBox.Text == "")
            {
                splitContainer.Panel2.Enabled = true;
                foreach (dynamic plugin in plugins_request) { pluginsBox.Items.Add(plugin.name); }
                pluginsBox.SelectedIndex = 0;
                return;
            }
            pluginsBox.Items.Clear();
            splitContainer.Panel2.Enabled = false;
        }
    }
}
