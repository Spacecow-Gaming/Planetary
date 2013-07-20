using System;
using SFML.Window;
using SFML.Graphics;
using System.Timers;

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
            RenderWindow WMenu =
                new RenderWindow(new VideoMode(640, 480), "Planetary");
            WMenu.SetVisible(true);

            // These are the buttons
            Texture TExit = new Texture("Media/exit.png");
            Sprite SExit = new Sprite(TExit);
            Texture TStart = new Texture("Media/start.png");
            Sprite SStart = new Sprite(TStart);

            // These are the nice-looking things which aren't strictly
            // necessary
            Texture TTitle = new Texture("Media/title.png");
            Sprite STitle = new Sprite(TTitle);
            Texture TBackground = new Texture("Media/menuback.png");
            Sprite SBackground = new Sprite(TBackground);

            // This is the actual button i.e. handles the clicks
            Button BExit = new Button(SExit, WMenu);
            Button BStart = new Button(SStart, WMenu);

            // Guess what happens when you close the window? It CLOSES!
            WMenu.Closed +=
                delegate(Object o, EventArgs e) { WMenu.Close(); };

            BExit.Click +=
                delegate(Object o, EventArgs e) { WMenu.Close(); };

            BStart.Click +=
                delegate(Object o, EventArgs e) { StartGame(WMenu); };


            while (WMenu.IsOpen())
            {
                // Handles input according to handlers set above
                WMenu.DispatchEvents();

                // Magic numbers? YES. Fuck the police.
                SBackground.Position = new Vector2f(0, 0);
                STitle.Position = new Vector2f(224, 0);
                SStart.Position = new Vector2f(288, 200);
                SExit.Position = new Vector2f(288, 240);

                // Renders everything
                WMenu.Clear(Color.Magenta);
                WMenu.Draw(SBackground);
                WMenu.Draw(STitle);
                WMenu.Draw(SStart);
                WMenu.Draw(SExit);
                WMenu.Display();
            }
        }

        /// <summary>
        /// Draws game, associated UI components
        /// </summary>
        /// 
        private void StartGame(Window WMenu)
        {

            // This is only done once, there is no need to make a method for it
            View view = new View
                           (new Vector2f(250, 250),      // Centre of the view
                            new Vector2f (640, -480));  // Size of the view

            // The ever-present background
            Texture TBackground = new Texture("Media/menuback.png");
            Sprite SBackground = new Sprite(TBackground);
            

            // Creates a new instance of the player
            Player Player1 = new Player("Media/ship.png");

            // Creates a new instance of the board
            Board GameBoard = new Board("Media/board.png");

            // Creates a new planet
            Planet NewPlanet = new Planet("Media/planet.png");

            // Creates the window and gives it certain properties
            RenderWindow WGame = new RenderWindow(new VideoMode(640, 480), "Planetary");
            WGame.Position = WMenu.Position;
            WMenu.SetVisible(false);
            WGame.Closed += delegate(Object o, EventArgs e)
                {
                    WMenu.Position = WGame.Position;
                    WMenu.SetVisible(true);
                    WGame.Close();
                };

            // Sets board to rotate when mouse is released
            // This avoids constant spinning if button is held down
            WGame.MouseButtonReleased += delegate(Object o, MouseButtonEventArgs e)
                {
                    if (e.Button == Mouse.Button.Left)
                        // The size of the rotation scales with the sector count
                        // This means the board looks correct
                        GameBoard.sprite.Rotation -= 360/(float)GameBoard.SectorCount;
                };
            WGame.SetView(view);

            while (WGame.IsOpen())
            {
                // Process events
                WGame.DispatchEvents();

                // Renders everything
                WGame.Draw(SBackground);
                WGame.Draw(GameBoard.sprite);
                WGame.Draw(Player1.sprite);
                WGame.Draw(NewPlanet.sprite);
                WGame.Display();

            }
        }
    }

    /// <summary>
    /// Click it, fires click event.
    /// </summary>
    class Button
    {
        private Sprite sprite;
        public event EventHandler Click;

        /// <summary>
        /// Adds handler to parent window to call OnClick
        /// </summary>
        /// <param name="InSprite">Sprite representing button</param>
        /// <param name="InWindow">Parent window</param>
        public Button(Sprite InSprite, Window InWindow)
        {
            sprite = InSprite;
            InWindow.MouseButtonPressed +=
                new EventHandler<MouseButtonEventArgs>(OnClick);
        }
        private void OnClick(object sender, MouseButtonEventArgs e)
        {
            switch (e.Button)
            {
                // There will be more cases, don't turn this into an if
                case Mouse.Button.Left:
                    if (sprite.GetGlobalBounds().Contains(e.X, e.Y))
                    {
                        Click(sender, e);
                    }
                    break;
                default:
                    break;
            }
        }
    }

}
