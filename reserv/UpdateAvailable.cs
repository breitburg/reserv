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
    public partial class UpdateAvailable : Form
    {
        public string downloadUrl;
        public UpdateAvailable(string changelog, string body, string downloadUrl)
        {
            InitializeComponent();
            this.downloadUrl = downloadUrl;
            changelogText.Text = changelog;
            versionLabel.Text = body;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process.Start(downloadUrl);
            this.Close();
        }
    }
}
