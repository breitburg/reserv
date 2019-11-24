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
namespace Reserv
{
    public partial class UploadPluginForm : Form
    {
        public UploadPluginForm()
        {
            InitializeComponent();
        }

        private void nameBox_TextChanged(object sender, EventArgs e) { bukkitNameBox.Text = nameBox.Text; }

        private void checkButton_Click(object sender, EventArgs e) { Process.Start("https://dev.bukkit.org/projects/" + bukkitNameBox.Text + "/files/latest"); }

        private void bukkitNameBox_TextChanged(object sender, EventArgs e) { checkButton.Enabled = bukkitNameBox.Text == "" ? false : true; }

        private void iconBox_TextChanged(object sender, EventArgs e) { pictureBox1.ImageLocation = iconBox.Text; }
    }
}
