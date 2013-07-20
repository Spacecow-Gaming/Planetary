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
    public int SectorCount;

    /// <summary>
    /// Initiates board sprite, texture, sectors
    /// </summary>
    /// <param name="ImgPath"></param>
    public Board(string ImgPath)
    {
        Texture texture = new Texture(ImgPath);
        sprite = new Sprite(texture);
        sprite.Origin = new Vector2f(500, 500);

        // TODO: Make this depend on number of players, or something
        SectorCount = 16;
    }
}


