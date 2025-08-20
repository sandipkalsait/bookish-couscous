namespace Assignment3_Q6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            // Load cities into ComboBox on form load
            this.Load += Form1_Load;

            // Button click event
            button1.Click += button1_Click;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Add city names
            comboBox1.Items.Add("Mumbai");
            comboBox1.Items.Add("Pune");
            comboBox1.Items.Add("Delhi");
            comboBox1.Items.Add("Bangalore");
            comboBox1.Items.Add("Chennai");
            comboBox1.Items.Add("Hyderabad");

            comboBox1.SelectedIndex = 0; // Default selection
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (comboBox1.SelectedItem != null)
            {
                string city = comboBox1.SelectedItem.ToString();
                MessageBox.Show($"You selected: {city}", "City Selected",
                                MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Please select a city.", "Error",
                                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
