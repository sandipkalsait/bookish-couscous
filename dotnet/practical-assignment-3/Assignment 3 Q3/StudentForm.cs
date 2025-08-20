using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace Asssignment_3_Q3
{
    public partial class StudentForm : Form
    {
        // Dictionary to map Streams -> Skills
        private readonly Dictionary<string, string[]> streamKnowledgeMap = new Dictionary<string, string[]>
        {
            { "MCA", new string[] { "VB.NET", "C#.NET", "J#.NET", "ASP.NET" } },
            { "MBA", new string[] { "Excel", "SAP", "Tally" } },
            { "MCM", new string[] { "C Programming", "Networking", "Data Structures" } },
            { "BCA", new string[] { "C", "C++", "Python" } }
        };

        public StudentForm()
        {
            InitializeComponent();

            // Attach radio button events
            radioButton1.CheckedChanged += RadioButton_CheckedChanged;
            radioButton2.CheckedChanged += RadioButton_CheckedChanged;
            radioButton3.CheckedChanged += RadioButton_CheckedChanged;
            radioButton4.CheckedChanged += RadioButton_CheckedChanged;

            // Attach button events
            button2.Click += button2_Click;
            button3.Click += button3_Click;
        }

        private void StudentForm_Load(object sender, EventArgs e)
        {
            textBox1.Text = string.Empty;  // clear name field
            LoadKnowledgeOptions("MCA");   // Default MCA
        }

        private void label1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Welcome to Student Profile Form", "Info",
                            MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void splitContainer1_Panel1_Paint(object sender, PaintEventArgs e) { }
        private void splitContainer1_Panel2_Paint(object sender, PaintEventArgs e) { }
        private void groupBox1_Enter(object sender, EventArgs e) { }
        private void groupBox2_Enter(object sender, EventArgs e) { }

        // Handle stream radio button change
        private void RadioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked) LoadKnowledgeOptions("MCA");
            else if (radioButton2.Checked) LoadKnowledgeOptions("MBA");
            else if (radioButton3.Checked) LoadKnowledgeOptions("MCM");
            else if (radioButton4.Checked) LoadKnowledgeOptions("BCA");
        }

        // Dynamically load checkboxes based on stream
        private void LoadKnowledgeOptions(string stream)
        {
            groupBox2.Controls.Clear();

            if (streamKnowledgeMap.ContainsKey(stream))
            {
                string[] skills = streamKnowledgeMap[stream];
                int y = 40;

                foreach (var skill in skills)
                {
                    CheckBox cb = new CheckBox();
                    cb.Text = skill;
                    cb.Font = new System.Drawing.Font("Calibri", 10F, System.Drawing.FontStyle.Bold);
                    cb.ForeColor = System.Drawing.Color.Black;
                    cb.AutoSize = true;
                    cb.Location = new System.Drawing.Point(40, y);

                    groupBox2.Controls.Add(cb);
                    y += 40;
                }
            }
        }

        // Submit button
        private void button1_Click(object sender, EventArgs e)
        {
            string name = textBox1.Text.Trim();

            string stream = "";
            if (radioButton1.Checked) stream = "MCA";
            else if (radioButton2.Checked) stream = "MBA";
            else if (radioButton3.Checked) stream = "MCM";
            else if (radioButton4.Checked) stream = "BCA";

            string knowledge = "";
            foreach (Control ctrl in groupBox2.Controls)
            {
                if (ctrl is CheckBox cb && cb.Checked)
                {
                    knowledge += cb.Text + " ";
                }
            }

            if (string.IsNullOrEmpty(name))
            {
                MessageBox.Show("Please enter your name.", "Validation Error",
                                MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            MessageBox.Show($"Name: {name}\nStream: {stream}\nKnowledge: {knowledge}",
                            "Student Profile",
                            MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        // Exit button
        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        // New button (reset form)
        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            radioButton1.Checked = true; // default MCA
            LoadKnowledgeOptions("MCA");
        }
    }
}
