using System;
using SFML.Window;
using SFML.Graphics;
using SFML.Audio;

/// <summary>
/// Generic matter base class
/// </summary>
class Matter
{
    public Sprite sprite { get; set; }

    // This represents the number of the square the object is on, on the board
    public int position { get; set; }

    public Matter(string ImgPath)
    {
        Random random = new Random();
        position = random.Next(0, 15);

        Texture texture = new Texture(ImgPath);
        sprite = new Sprite(texture);

        // Sets the position of the player's ship when it starts... magic numbers...
        sprite.Position = new Vector2f(300, 50);
        sprite.Rotation = 180;
    }
}

/// <summary>
/// Generic ship base class, controlled by no-one
/// </summary>
class Ship : Matter
{
    public Ship(string ImgPath)
        : base(ImgPath)
    {

    }
}

/// <summary>
/// The player flies this around and has fun
/// </summary>
class Player : Ship
{
    public Player(string ImgPath)
        : base(ImgPath)
    {

    }


}

/// <summary>
/// Robots powered by magic use these
/// </summary>
class AIShip : Ship
{
    public AIShip(string ImgPath)
        : base(ImgPath)
    {

    }

}

/// <summary>
/// Scenic destinations for players to visit
/// </summary>
class Planet : Matter
{
    public Planet(string ImgPath)
        : base(ImgPath)
    {
        // TODO: Put planet on board according to position var

        sprite.Position = new Vector2f(430, 430);
    }
}
