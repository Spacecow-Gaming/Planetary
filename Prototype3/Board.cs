using SFML.Window;
using SFML.Graphics;

/// <summary>
/// Contains lists of objects, data about sector
/// </summary>
class Sector
{

}

/// <summary>
/// Contains some sectors and other data
/// </summary>
class Board
{
    public Sprite sprite { get; set; }

    /// <summary>
    /// Initiates board sprite, texture, sectors
    /// </summary>
    /// <param name="ImgPath"></param>
    public Board(string ImgPath)
    {
        Texture texture = new Texture(ImgPath);
        sprite = new Sprite(texture);
    }
}


