using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Planetary
{
    public partial class PlanetaryMenuForm : Form
    {
        public PlanetaryMenuForm()
        {
            InitializeComponent();
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            this.Hide();
            PlanetaryGameForm GameForm = new PlanetaryGameForm();
            GameForm.StartPosition = FormStartPosition.Manual;
            GameForm.Location = this.Location;
            GameForm.ShowDialog(this);
        }
    }
}
