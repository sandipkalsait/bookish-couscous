namespace Assignment_3_Q3
{
    public partial class ArithmaticOpsForm : Form
    {
        public ArithmaticOpsForm()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(textBox1.Text))
            {
                MessageBox.Show("Please enter a number first.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int number = Convert.ToInt32(textBox1.Text);

            if (radioPalindrome.Checked)
            {
                // Palindrome check
                string original = number.ToString();
                string reversed = new string(original.Reverse().ToArray());

                if (original == reversed)
                    MessageBox.Show($"{number} is a Palindrome.", "Result", MessageBoxButtons.OK, MessageBoxIcon.Information);
                else
                    MessageBox.Show($"{number} is NOT a Palindrome.", "Result", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else if (radioPerfect.Checked)
            {
                // Perfect number check
                int sum = 0;
                for (int i = 1; i <= number / 2; i++)
                {
                    if (number % i == 0)
                        sum += i;
                }

                if (sum == number)
                    MessageBox.Show($"{number} is a Perfect Number.", "Result", MessageBoxButtons.OK, MessageBoxIcon.Information);
                else
                    MessageBox.Show($"{number} is NOT a Perfect Number.", "Result", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else if (radioArmstrong.Checked)
            {
                // Armstrong number check
                int temp = number;
                int sum = 0;
                int digits = number.ToString().Length;

                while (temp > 0)
                {
                    int digit = temp % 10;
                    sum += (int)Math.Pow(digit, digits);
                    temp /= 10;
                }

                if (sum == number)
                    MessageBox.Show($"{number} is an Armstrong Number.", "Result", MessageBoxButtons.OK, MessageBoxIcon.Information);
                else
                    MessageBox.Show($"{number} is NOT an Armstrong Number.", "Result", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                MessageBox.Show("Please select one of the options (Palindrome, Perfect, Armstrong).", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }


        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
