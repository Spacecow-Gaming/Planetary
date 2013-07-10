using SFML.Window;
using SFML.Graphics;

/// <summary>
/// Contains some sectors and other data
/// </summary>
class Board
{
    public Sprite SBoard { get; set; }
    public Board(string ImgPath)
    {
        Texture TBoard = new Texture(ImgPath);
        SBoard = new Sprite(TBoard);
    }

}

/// <summary>
/// Contains lists of objects, data about sector
/// </summary>
class Sector
{

}