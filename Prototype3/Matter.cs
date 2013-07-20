using System;
using SFML.Window;
using SFML.Graphics;
using SFML.Audio;

/// <summary>
/// Generic matter base class
/// </summary>
class Matter
{

}

/// <summary>
/// Generic ship base class, controlled by no-one
/// </summary>
class Ship : Matter
{

}

/// <summary>
/// The player flies this around and has fun
/// </summary>
class Player : Ship
{
    public Sprite sprite { get; set; }

    public Player(string ImgPath)
    {
        Texture texture = new Texture(ImgPath);
        sprite = new Sprite(texture);

        // Sets the position of the player's ship when it starts... magic numbers...
        sprite.Position = new Vector2f(300, 50);
        sprite.Rotation = 180;
    }
}

/// <summary>
/// Robots powered by magic use these
/// </summary>
class AIShip : Ship
{

}

/// <summary>
/// Scenic destinations for players to visit
/// </summary>
class Planet : Matter
{
    public Sprite sprite { get; set; }

    // This represents the number of the square the planet is on, on the board
    public int position { get; set; }

    public Planet(string imgPath)
    {
        Random random = new Random();
        position = random.Next(0, 15);

        Texture texture = new Texture(imgPath);
        sprite = new Sprite(texture);

        //sprite.Position = planetPosition;
        sprite.Position = new Vector2f(430, 430);
    }
}
