using System;
using SFML.Window;
using SFML.Graphics;
using System.Timers;

/// <summary>
/// This is actually a singleton
/// </summary>
class Game
{
    /// <summary>
    /// Draws game, associated UI components
    /// </summary>
    public void Start(Window WMenu)
    {
        View view = new View
                       (new Vector2f(250, 250),    // Centre of the view
                        new Vector2f(640, -480));  // Size of the view

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
                    GameBoard.sprite.Rotation -= 360 / (float)GameBoard.SectorCount;
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
/// Interactive image. You can mouse over it, click on it etc.
/// </summary>
class AdvImage
{
    public Sprite sprite { get; set; }
    public event EventHandler Click;

    /// <summary>
    /// Adds handler to parent window to call OnClick
    /// </summary>
    /// <param name="InSprite">Sprite representing button</param>
    /// <param name="InWindow">Parent window</param>
    public AdvImage(string ImgPath, Window InWindow)
    {
        Texture texture = new Texture(ImgPath);
        sprite = new Sprite(texture);
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
