using System;

namespace Planetary
{
    /// <summary>
    /// Generic matter class
    /// </summary>
    class Matter
    {
        public Matter()
        {
            
        }
    }

    /// <summary>
    /// Ship which can be AI run or player run
    /// </summary>
    class Ship : Matter
    {

    }

    /// <summary>
    /// What the player controls
    /// </summary>
    class Player : Ship
    {

    }

    /// <summary>
    /// Scenic locations for players to visit
    /// </summary>
    class Planet : Matter
    {

    }
}