namespace Assignment_3_Q2
{
    public partial class StringOpsForm : Form
    {
        public StringOpsForm()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str1 = textBox1.Text;
            string str2 = textBox2.Text;
            textBox3.Text = string.Concat(str1, str2);
            MessageBox.Show("Strings concatenated successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }


        private void button4_Click(object sender, EventArgs e)
        {

            this.Close();
        }

        private void label3_Click(object sender, EventArgs e)
        {


        }


        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            textBox2.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string str1 = textBox1.Text;
            string str2 = textBox2.Text;

            string reversedStr1 = new string(str1.Reverse().ToArray());
            string reversedStr2 = new string(str2.Reverse().ToArray());

            textBox3.Text = reversedStr1 + "," + reversedStr2;

            MessageBox.Show("Strings reversed successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
