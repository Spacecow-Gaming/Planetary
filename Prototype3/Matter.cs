using System;

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

}