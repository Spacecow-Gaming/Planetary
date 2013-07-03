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
    public partial class PlanetaryGameForm : Form
    {
        public PlanetaryGameForm()
        {
            InitializeComponent();
        }

        private void ToMenuButton_Click(object sender, EventArgs e)
        {
            Owner.Show();
            this.Close();
        }
    }
}
