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
            RenderWindow MenuWindow = 
                new RenderWindow(new VideoMode(640, 480), "Planetary");
            MenuWindow.SetVisible(true);
            MenuWindow.Closed += 
                delegate(Object o, EventArgs e) { MenuWindow.Close(); };

            // These are the buttons
            Texture ExitT = new Texture("Media/exit.png");
            Sprite ExitS = new Sprite(ExitT);
            Texture StartT = new Texture("Media/start.png");
            Sprite StartS = new Sprite(StartT);

            // These are the nice-looking things which aren't strictly
            // necessary
            Texture TitleT = new Texture("Media/title.png");
            Sprite TitleS = new Sprite(TitleT);
            Texture BackgroundT = new Texture("Media/menuback.png");
            Sprite BackgroundS = new Sprite(BackgroundT);

            while (MenuWindow.IsOpen())
            {
                MenuWindow.DispatchEvents();
                BackgroundS.Position = new Vector2f(0, 0);
                TitleS.Position = new Vector2f(224, 0);
                StartS.Position = new Vector2f(288, 200);
                ExitS.Position = new Vector2f(288, 240);
                MenuWindow.Draw(BackgroundS);
                MenuWindow.Draw(TitleS);
                MenuWindow.Draw(StartS);
                MenuWindow.Draw(ExitS);
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
