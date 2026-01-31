namespace Warehouse
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            warehouseappLabel = new Label();
            textBox1 = new TextBox();
            label1 = new Label();
            label2 = new Label();
            textBox2 = new TextBox();
            SuspendLayout();
            // 
            // warehouseappLabel
            // 
            warehouseappLabel.AutoSize = true;
            warehouseappLabel.Location = new Point(290, 66);
            warehouseappLabel.Name = "warehouseappLabel";
            warehouseappLabel.Size = new Size(147, 25);
            warehouseappLabel.TabIndex = 0;
            warehouseappLabel.Text = "Ware House App";
            warehouseappLabel.Click += label1_Click;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(322, 119);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(278, 31);
            textBox1.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(144, 125);
            label1.Name = "label1";
            label1.Size = new Size(134, 25);
            label1.TabIndex = 2;
            label1.Text = "Enter username";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(144, 179);
            label2.Name = "label2";
            label2.Size = new Size(132, 25);
            label2.TabIndex = 4;
            label2.Text = "Enter Password";
            label2.Click += this.label2_Click;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(322, 173);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(278, 31);
            textBox2.TabIndex = 3;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label2);
            Controls.Add(textBox2);
            Controls.Add(label1);
            Controls.Add(textBox1);
            Controls.Add(warehouseappLabel);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        protected internal Label warehouseappLabel;
        private TextBox textBox1;
        protected internal Label label1;
        protected internal Label label2;
        private TextBox textBox2;
        private Label WareHouse;
    }
}
