namespace Assignment_3_Q3
{
    partial class ArithmaticOpsForm
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
            textBox1 = new TextBox();
            radioPalindrome = new RadioButton();
            radioPerfect = new RadioButton();
            radioArmstrong = new RadioButton();
            button1 = new Button();
            button2 = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(191, 111);
            label1.Name = "label1";
            label1.Size = new Size(77, 25);
            label1.TabIndex = 0;
            label1.Text = "Number";
            // 
            // textBox1
            // 
            textBox1.Location = new Point(342, 105);
            textBox1.Name = "textBox1";
            textBox1.PlaceholderText = "Enter the number here";
            textBox1.Size = new Size(230, 31);
            textBox1.TabIndex = 1;
            textBox1.TextAlign = HorizontalAlignment.Center;
            // 
            // radioPalindrome
            // 
            radioPalindrome.AutoSize = true;
            radioPalindrome.Location = new Point(342, 176);
            radioPalindrome.Name = "radioPalindrome";
            radioPalindrome.Size = new Size(199, 29);
            radioPalindrome.TabIndex = 2;
            radioPalindrome.TabStop = true;
            radioPalindrome.Text = "Palindrome Number";
            radioPalindrome.UseVisualStyleBackColor = true;
            // 
            // radioPerfect
            // 
            radioPerfect.AutoSize = true;
            radioPerfect.Location = new Point(342, 211);
            radioPerfect.Name = "radioPerfect";
            radioPerfect.Size = new Size(161, 29);
            radioPerfect.TabIndex = 3;
            radioPerfect.TabStop = true;
            radioPerfect.Text = "Perfect Number";
            radioPerfect.UseVisualStyleBackColor = true;
            // 
            // radioArmstrong
            // 
            radioArmstrong.AutoSize = true;
            radioArmstrong.Location = new Point(342, 246);
            radioArmstrong.Name = "radioArmstrong";
            radioArmstrong.Size = new Size(201, 29);
            radioArmstrong.TabIndex = 4;
            radioArmstrong.TabStop = true;
            radioArmstrong.Text = "Armstrong Number";
            radioArmstrong.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            button1.Location = new Point(234, 312);
            button1.Name = "button1";
            button1.Size = new Size(112, 34);
            button1.TabIndex = 5;
            button1.Text = "OK";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(425, 312);
            button2.Name = "button2";
            button2.Size = new Size(112, 34);
            button2.TabIndex = 6;
            button2.Text = "Exit";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // ArithmaticOpsForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(radioArmstrong);
            Controls.Add(radioPerfect);
            Controls.Add(radioPalindrome);
            Controls.Add(textBox1);
            Controls.Add(label1);
            Name = "ArithmaticOpsForm";
            Text = "Arithmatic Operations App";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private TextBox textBox1;
        private RadioButton radioPalindrome;
        private RadioButton radioPerfect;
        private RadioButton radioArmstrong;
        private Button button1;
        private Button button2;
    }
}
