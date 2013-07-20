using System;
using SFML.Window;
using SFML.Graphics;

class MainMenu
{
    /// <summary>
    /// The entry point of the program
    /// </summary>
    /// <param name="args">Command line arguments</param>
    static void Main(String[] args)
    {
        MainMenu menu = new MainMenu();
    }

    public MainMenu()
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

        // Loads up the game and its files etc, will be started soon
        Game MainGame = new Game();

        // Guess what happens when you close the window? It CLOSES!
        WMenu.Closed +=
            delegate(Object o, EventArgs e) { WMenu.Close(); };

        BExit.Click +=
            delegate(Object o, EventArgs e) { WMenu.Close(); };

        BStart.Click +=
            delegate(Object o, EventArgs e) { MainGame.Start(WMenu); };


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
}