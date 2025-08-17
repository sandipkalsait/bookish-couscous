using System;
using System.Windows.Forms;

namespace Assignment_3
{
    public partial class CalculatorForm : Form
    {
        public CalculatorForm()
        {
            InitializeComponent();
        }

        // Add
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                double n1 = Convert.ToDouble(textBox1.Text);
                double n2 = Convert.ToDouble(textBox2.Text);
                textBox3.Text = (n1 + n2).ToString();
            }
            catch
            {
                MessageBox.Show("Please enter valid numbers.", "Error");
            }
        }

        // Subtract
        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                double n1 = Convert.ToDouble(textBox1.Text);
                double n2 = Convert.ToDouble(textBox2.Text);
                textBox3.Text = (n1 - n2).ToString();
            }
            catch
            {
                MessageBox.Show("Please enter valid numbers.", "Error");
            }
        }

        // Multiply
        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                double n1 = Convert.ToDouble(textBox1.Text);
                double n2 = Convert.ToDouble(textBox2.Text);
                textBox3.Text = (n1 * n2).ToString();
            }
            catch
            {
                MessageBox.Show("Please enter valid numbers.", "Error");
            }
        }

        // Divide
        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                double n1 = Convert.ToDouble(textBox1.Text);
                double n2 = Convert.ToDouble(textBox2.Text);
                if (n2 == 0)
                {
                    MessageBox.Show("Cannot divide by zero.", "Error");
                }
                else
                {
                    textBox3.Text = (n1 / n2).ToString();
                }
            }
            catch
            {
                MessageBox.Show("Please enter valid numbers.", "Error");
            }
        }

        // Reset
        private void button5_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox1.Focus();
        }

        // Exit
        private void button6_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void titleLabel_Click(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void flowLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void titleLabel_Click_1(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }
    }
}
