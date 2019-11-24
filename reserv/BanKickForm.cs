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
    public partial class BanKickForm : Form
    {
        public bool isClicked = false;
        public BanKickForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            isClicked = true;
            this.Close();
        }
    }
}
