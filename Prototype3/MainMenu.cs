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

    private RenderWindow window;

    public MainMenu()
    {
        window =
            new RenderWindow(new VideoMode(640, 480), "Planetary");
        window.SetVisible(true);

        // These are the nice-looking things
        Sprite Title = new Sprite(new Texture("Media/title.png"));
        Sprite Background = new Sprite(new Texture("Media/menuback.png"));

        // These are buttons
        AdvImage BExit = new AdvImage("Media/exit.png", window);
        AdvImage BStart = new AdvImage("Media/Start.png", window);

        // Loads up the game and its files etc, will be started soon
        Game MainGame = new Game();

        // Guess what happens when you close the window? It CLOSES!
        window.Closed +=
            delegate(Object o, EventArgs e) { window.Close(); };

        BExit.Click +=
            delegate(Object o, EventArgs e) { window.Close(); };

        BStart.Click +=
            delegate(Object o, EventArgs e) { MainGame.Start(window); };


        while (window.IsOpen())
        {
            // Handles input according to handlers set above
            window.DispatchEvents();

            // Magic numbers? YES. Fuck the police.
            Background.Position = new Vector2f(0, 0);
            Title.Position = new Vector2f(224, 0);
            BStart.sprite.Position = new Vector2f(288, 200);
            BExit.sprite.Position = new Vector2f(288, 240);

            // Renders everything
            window.Clear(Color.Magenta);
            window.Draw(Background);
            window.Draw(Title);
            window.Draw(BExit.sprite);
            window.Draw(BStart.sprite);
            window.Display();
        }

    }
}