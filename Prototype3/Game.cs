using System;
using SFML.Window;
using SFML.Graphics;

namespace Planetary
{
    /// <summary>
    /// This is actually a singleton
    /// </summary>
    class PlanetaryGame
    {
        /// <summary>
        /// The entry point of the program
        /// </summary>
        static void Main(string[] args)
        {
            PlanetaryGame Game = new PlanetaryGame();
        }

        /// <summary>
        /// Ctor which starts the main menu
        /// </summary>
        public PlanetaryGame()
        {
            MainMenu();
        }

        /// <summary>
        /// Draws main menu window, associated buttons
        /// </summary>
        private void MainMenu()
        {
            Window MenuWindow = 
                new Window(new VideoMode(640, 480), "Planetary");
            MenuWindow.SetVisible(true);
            MenuWindow.Closed += 
                delegate(Object o, EventArgs e) { MenuWindow.Close(); };

            while (MenuWindow.IsOpen())
            {
                MenuWindow.DispatchEvents();
                MenuWindow.Display();
            }
        }

        /// <summary>
        /// Draws game, associated UI components
        /// </summary>
        private void StartGame()
        {

        }
    }

    /// <summary>
    /// Contains some sectors and other data
    /// </summary>
    class Board
    {

    }

    /// <summary>
    /// Contains lists of objects, data about sector
    /// </summary>
    class Sector
    {

    }
}
