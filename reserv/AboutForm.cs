using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reserv
{
    public partial class AboutForm : Form
    {
        public AboutForm()
        {
            InitializeComponent();
            versionLabel.Text = Application.ProductVersion;
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("http://upbits.org/reserv/");
        }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("https://vk.com/upbits");
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            Random random = new Random();
            pictureBox1.Location = new Point(random.Next(0, (this.Size.Width - pictureBox1.Size.Width)), random.Next(0, (this.Size.Height - pictureBox1.Size.Height))); 
            // MessageBox.Show("lala");
        }
    }
}
