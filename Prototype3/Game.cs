﻿using System;
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

        int timeLeft = 60;

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

            // Creates a new 2d Camera (used for rotation and much much more)
            Vector2f centre = new Vector2f(250, 250);
            Vector2f size = new Vector2f(500, -500);

            View view = new View(centre, size);

            // Creates a new instance of the player
            Player Player1 = new Player("Media/ship.png");

            // Creates a new instance of the board
            Board GameBoard = new Board("Media/boardTest.png");

            // Sets the position of the player's ship when it starts... magic numbers...
            Player1.sprite.Position = new Vector2f(300, 50);
            Player1.sprite.Rotation = 180;

            // Creates the window and gives it certain properties
            RenderWindow WGame = new RenderWindow(new VideoMode(500, 500), "Planetary");
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
                Timer timer = new Timer();
                timer.Elapsed += new ElapsedEventHandler(OnTimedEvent);
                timer.Interval = 1000;
                timer.Enabled = true;
                timer.Start();

                Vector2f textPos = new Vector2f(400, 400);
                Font font = new Font("Media/Arial.ttf");
                Text text = new Text();
                text.Font = font;
                text.DisplayedString = timeLeft.ToString();
                text.CharacterSize = 35;
                text.Color = (Color.Yellow);
                text.Position = textPos;
                text.Rotation = 180;

                var origin = new Vector2f(500, 500);
                GameBoard.sprite.Origin = origin;

                WGame.SetView(view);

                // Process events
                WGame.DispatchEvents();

                // Updates world

                // Renders everything
                WGame.Draw(GameBoard.sprite);
                WGame.Draw(Player1.sprite);
                WGame.Draw(text);
                WGame.Display();

                if (Mouse.IsButtonPressed(Mouse.Button.Left))
                {
                    GameBoard.sprite.Rotation = GameBoard.sprite.Rotation - 15;
                }
            }
        }

        private void OnTimedEvent(object sender, ElapsedEventArgs e)
        {
            timeLeft = timeLeft - 1;
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
