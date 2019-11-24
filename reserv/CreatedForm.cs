using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reserv
{
    public partial class CreatedForm : Form
    {
        public CreatedForm(string serverName, string serverVersion, string maxPlayers, string pluginsCount)
        {
            InitializeComponent();
            serverNameLabel.Text = serverName;
            maxplayersLabel.Text = maxPlayers;
            pluginsCountLabel.Text = pluginsCount;
            versionLabel.Text = serverVersion;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
