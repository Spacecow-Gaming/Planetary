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
        private void StartGame(Window WMenu)
        {
            // Creates a new instance of the player
            var player = new Player();
            
            // The Texture and Sprite for the background
            Texture TBoard = new Texture("Media/board1.png");
            Sprite SBoard = new Sprite(TBoard);

            // Sets the position of the player's ship when it starts... magic numbers...
            player.SPlayer.Position = new Vector2f(270, 440);

            

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

            while (WGame.IsOpen())
            {
                // Process events
                WGame.DispatchEvents();

                // Updates world

                // Renders everything
                WGame.Clear(Color.Magenta);
                WGame.Draw(SBoard);
                WGame.Draw(player.SPlayer);
                WGame.Display();
            }
        }
    }

    /// <summary>
    /// Click it, fires click event.
    /// </summary>
    class Button
    {
        private Sprite MySprite;
        public event EventHandler Click;

        /// <summary>
        /// Adds handler to parent window to call OnClick
        /// </summary>
        /// <param name="InSprite"></param>
        /// <param name="InWindow"></param>
        public Button(Sprite InSprite, Window InWindow)
        {
            MySprite = InSprite;
            InWindow.MouseButtonPressed +=
                new EventHandler<MouseButtonEventArgs>(OnClick);
        }
        private void OnClick(object sender, MouseButtonEventArgs e)
        {
            switch (e.Button)
            {
                case Mouse.Button.Left:
                    if (MySprite.GetGlobalBounds().Contains(e.X, e.Y))
                    {
                        Click(sender, e);
                    }
                    break;
                default:
                    break;
            }
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
