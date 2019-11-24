namespace Reserv
{
    partial class ProcessingForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.cancelButton = new System.Windows.Forms.Button();
            this.progressBar = new System.Windows.Forms.ProgressBar();
            this.processLabel = new System.Windows.Forms.Label();
            this.allBar = new System.Windows.Forms.ProgressBar();
            this.label1 = new System.Windows.Forms.Label();
            this.installPlugins = new System.ComponentModel.BackgroundWorker();
            this.stepLabel = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.panel1.BackColor = System.Drawing.SystemColors.Control;
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.cancelButton);
            this.panel1.Location = new System.Drawing.Point(-3, 200);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(484, 85);
            this.panel1.TabIndex = 4;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(21, 28);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(340, 39);
            this.label3.TabIndex = 1;
            this.label3.Text = "Пожалуйста, подождите пока Reserv настраивает ваш сервер.\r\nПроцесс может занять н" +
    "екоторое время, так что вы можете\r\nприготовить и попить чай, либо посмотреть тре" +
    "нды на YouTube.";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.Location = new System.Drawing.Point(20, 11);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(68, 13);
            this.label2.TabIndex = 0;
            this.label2.Text = "Ожидайте";
            // 
            // cancelButton
            // 
            this.cancelButton.Location = new System.Drawing.Point(382, 34);
            this.cancelButton.Name = "cancelButton";
            this.cancelButton.Size = new System.Drawing.Size(75, 23);
            this.cancelButton.TabIndex = 7;
            this.cancelButton.Text = "Отмена";
            this.cancelButton.UseVisualStyleBackColor = true;
            this.cancelButton.Click += new System.EventHandler(this.cancelButton_Click);
            // 
            // progressBar
            // 
            this.progressBar.Location = new System.Drawing.Point(22, 54);
            this.progressBar.Name = "progressBar";
            this.progressBar.Size = new System.Drawing.Size(426, 23);
            this.progressBar.TabIndex = 6;
            // 
            // processLabel
            // 
            this.processLabel.AutoSize = true;
            this.processLabel.Location = new System.Drawing.Point(19, 38);
            this.processLabel.Name = "processLabel";
            this.processLabel.Size = new System.Drawing.Size(65, 13);
            this.processLabel.TabIndex = 5;
            this.processLabel.Text = "Загрузка...";
            // 
            // allBar
            // 
            this.allBar.Location = new System.Drawing.Point(22, 119);
            this.allBar.Name = "allBar";
            this.allBar.Size = new System.Drawing.Size(426, 23);
            this.allBar.TabIndex = 9;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(19, 103);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 13);
            this.label1.TabIndex = 8;
            this.label1.Text = "Общий процесс:";
            // 
            // installPlugins
            // 
            this.installPlugins.WorkerReportsProgress = true;
            this.installPlugins.WorkerSupportsCancellation = true;
            this.installPlugins.DoWork += new System.ComponentModel.DoWorkEventHandler(this.installPlugins_DoWork);
            this.installPlugins.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.installPlugins_ProgressChanged);
            this.installPlugins.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.installPlugins_RunWorkerCompleted);
            // 
            // stepLabel
            // 
            this.stepLabel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.stepLabel.AutoSize = true;
            this.stepLabel.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.stepLabel.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.stepLabel.Location = new System.Drawing.Point(382, 103);
            this.stepLabel.Name = "stepLabel";
            this.stepLabel.Size = new System.Drawing.Size(66, 13);
            this.stepLabel.TabIndex = 10;
            this.stepLabel.Text = "Шаг 0 из 4";
            this.stepLabel.TextAlign = System.Drawing.ContentAlignment.TopRight;
            // 
            // ProcessingForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(479, 284);
            this.ControlBox = false;
            this.Controls.Add(this.stepLabel);
            this.Controls.Add(this.allBar);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.progressBar);
            this.Controls.Add(this.processLabel);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "ProcessingForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Процесс Reserv";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ProgressBar progressBar;
        private System.Windows.Forms.Label processLabel;
        private System.Windows.Forms.Button cancelButton;
        private System.Windows.Forms.ProgressBar allBar;
        private System.Windows.Forms.Label label1;
        private System.ComponentModel.BackgroundWorker installPlugins;
        private System.Windows.Forms.Label stepLabel;
    }
}