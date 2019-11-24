using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reserv
{
    public partial class IPShowForm : Form
    {
        public IPShowForm()
        {
            InitializeComponent();
            IPAddress[] localIPs = Dns.GetHostAddresses(Dns.GetHostName());
            foreach (IPAddress addr in localIPs)
            {
                if (addr.AddressFamily == AddressFamily.InterNetwork)
                {
                    localBox.Text = addr.ToString();
                }
            }
            new Thread(() =>
            {
                try
                {
                    using (WebClient client = new WebClient())
                    {
                        string request = client.DownloadString("http://checkip.dyndns.org");
                        string[] a = request.ToString().Split(':');
                        string a2 = a[1].Substring(1);
                        string[] a3 = a2.Split('<');
                        string a4 = a3[0];
                        this.Invoke((Action)(() => { publicBox.Enabled = true; }));
                        this.Invoke((Action)(() => { label3.Visible = true; }));
                        this.Invoke((Action)(() => { linkLabel1.Visible = true; }));
                        this.Invoke((Action)(() => { publicBox.Text = a4; }));
                    }
                }
                catch (Exception)
                {
                    this.Invoke((Action)(() => { publicBox.Text = "Ошибка получения внешнего IP"; }));
                }
            }).Start();
    }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("http://g.zeos.in/?q=%D0%9A%D0%B0%D0%BA%20%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D1%8C%20%D0%BF%D0%BE%D1%80%D1%82%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B0%20Minecraft%3F");
        }
    }
}
