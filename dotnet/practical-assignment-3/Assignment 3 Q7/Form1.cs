namespace Assignment_3_Q7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void monthCalendar1_DateSelected(object sender, DateRangeEventArgs e)
        {
            // Get selected date
            DateTime selectedDate = monthCalendar1.SelectionStart;

            // Show in label
            label1.Text = "Selected Date: " + selectedDate.ToShortDateString();

            // Show in dialog
            MessageBox.Show("You selected: " + selectedDate.ToLongDateString(),
                            "Date Selected",
                            MessageBoxButtons.OK,
                            MessageBoxIcon.Information);
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
