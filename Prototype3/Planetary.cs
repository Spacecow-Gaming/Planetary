using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Windows.Forms;

namespace Planetary
{
    class Planetary
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Planetary Game = new Planetary();
            Game.MainMenu();
        }

        /// <summary>
        /// Displays main menu, starting game when startgame button is pressed
        /// </summary>
        private void MainMenu()
        {
            PlanetaryMenuForm MenuForm = new PlanetaryMenuForm();
            MenuForm.ShowDialog();
        }
    }
}
