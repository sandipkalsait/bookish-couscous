using System;
using System.Linq;
using System.Windows.Forms;

namespace Assignment_3_Q4
{
    public partial class ListOpsForm : Form
    {
        public ListOpsForm()
        {
            InitializeComponent();

        }

        private void Button1_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(textBox1.Text))
            {
                MessageBox.Show("Please add number first !");
            }else if (!string.IsNullOrWhiteSpace(textBox1.Text))
            {
                listView1.View = View.List;
                listView1.Items.Add(textBox1.Text.Trim());
                textBox1.Clear();
            }
           
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            if (listView1.Items.Count > 0) 
            {
                var numbers = listView1.Items.Cast<ListViewItem>()
                                             .Select(item => int.Parse(item.Text));
                MessageBox.Show("Minimum value: " + numbers.Min());
            }
            else
            {
               MessageBox.Show("No numbers in the list.");
            }
        }

        private void Button3_Click(object sender, EventArgs e)
        {
            if (listView1.Items.Count > 0)
            {
                var numbers = listView1.Items.Cast<ListViewItem>()
                                         .Select(item => int.Parse(item.Text));
                MessageBox.Show("Maximum value: " + numbers.Max());
            }
            else
            {
                MessageBox.Show("No numbers in the list.");
            }
        }
        private void button4_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();
            textBox1.Clear();
            MessageBox.Show("List cleared.");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }




    }
}
