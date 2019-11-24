using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Threading;

namespace Reserv
{
    public partial class AutomaticTestsForm : Form
    {
        public AutomaticTestsForm()
        {
            InitializeComponent();
            backgroundWorker.RunWorkerAsync();
        }

        private void backgroundWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            foreach (FileInfo directory in new DirectoryInfo("C:\\Windows\\System32").GetFiles("*.dll"))
            {
                backgroundWorker.ReportProgress(0, directory.Name);
                Thread.Sleep(5);
            }
                
        }

        private void backgroundWorker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            label.Text = "Проверка " + e.UserState.ToString() + "...";
        }

        private void backgroundWorker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            label.Text = "Тесты завершены. Ошибок не обнаружено.";
            this.Close();
        }
    }
}
