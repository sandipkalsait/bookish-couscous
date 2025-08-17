namespace Assignment_3_Q2
{
    partial class StringOpsForm
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
            label1 = new Label();
            label2 = new Label();
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            button4 = new Button();
            textBox3 = new TextBox();
            label3 = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            label1.AutoEllipsis = true;
            label1.AutoSize = true;
            label1.Location = new Point(205, 60);
            label1.Name = "label1";
            label1.Size = new Size(73, 25);
            label1.TabIndex = 0;
            label1.Text = "String 1";
            label1.TextAlign = ContentAlignment.MiddleCenter;
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            label2.AutoEllipsis = true;
            label2.AutoSize = true;
            label2.Location = new Point(205, 123);
            label2.Name = "label2";
            label2.Size = new Size(73, 25);
            label2.TabIndex = 1;
            label2.Text = "String 2";
            label2.TextAlign = ContentAlignment.MiddleCenter;
            label2.Click += label2_Click;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(392, 57);
            textBox1.Name = "textBox1";
            textBox1.PlaceholderText = "Enter the value here";
            textBox1.Size = new Size(224, 31);
            textBox1.TabIndex = 2;
            textBox1.TextAlign = HorizontalAlignment.Center;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(392, 114);
            textBox2.Name = "textBox2";
            textBox2.PlaceholderText = "Enter the value here";
            textBox2.Size = new Size(224, 31);
            textBox2.TabIndex = 3;
            textBox2.TextAlign = HorizontalAlignment.Center;
            // 
            // button1
            // 
            button1.Location = new Point(238, 292);
            button1.Name = "button1";
            button1.Size = new Size(135, 42);
            button1.TabIndex = 4;
            button1.Text = "Concatenate";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(408, 292);
            button2.Name = "button2";
            button2.Size = new Size(136, 42);
            button2.TabIndex = 5;
            button2.Text = "Reverse";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // button3
            // 
            button3.Location = new Point(238, 360);
            button3.Name = "button3";
            button3.Size = new Size(135, 42);
            button3.TabIndex = 6;
            button3.Text = "Clear";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // button4
            // 
            button4.Location = new Point(408, 360);
            button4.Name = "button4";
            button4.Size = new Size(135, 42);
            button4.TabIndex = 7;
            button4.Text = "Exit";
            button4.UseVisualStyleBackColor = true;
            button4.Click += button4_Click;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(392, 199);
            textBox3.Name = "textBox3";
            textBox3.ReadOnly = true;
            textBox3.Size = new Size(224, 31);
            textBox3.TabIndex = 9;
            textBox3.TextAlign = HorizontalAlignment.Center;
            textBox3.UseWaitCursor = true;
            // 
            // label3
            // 
            label3.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            label3.AutoEllipsis = true;
            label3.AutoSize = true;
            label3.Location = new Point(219, 199);
            label3.Name = "label3";
            label3.Size = new Size(59, 25);
            label3.TabIndex = 8;
            label3.Text = "Result";
            label3.TextAlign = ContentAlignment.MiddleCenter;
            label3.Click += label3_Click;
            // 
            // StringOpsForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(textBox3);
            Controls.Add(label3);
            Controls.Add(button4);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "StringOpsForm";
            Text = "String Operations App";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private TextBox textBox1;
        private TextBox textBox2;
        private Button button1;
        private Button button2;
        private Button button3;
        private Button button4;
        private TextBox textBox3;
        private Label label3;
    }
}
