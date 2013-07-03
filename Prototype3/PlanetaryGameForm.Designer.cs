namespace Planetary
{
    partial class PlanetaryGameForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.MineButton = new System.Windows.Forms.Button();
            this.ScanButton = new System.Windows.Forms.Button();
            this.TalkButton = new System.Windows.Forms.Button();
            this.AttackButton = new System.Windows.Forms.Button();
            this.ShipBox = new System.Windows.Forms.GroupBox();
            this.MapBox = new System.Windows.Forms.GroupBox();
            this.InfoBox = new System.Windows.Forms.GroupBox();
            this.InfoText = new System.Windows.Forms.Label();
            this.MoveButton = new System.Windows.Forms.Button();
            this.MoveCoordsInput = new System.Windows.Forms.TextBox();
            this.ToMenuButton = new System.Windows.Forms.Button();
            this.InfoBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // MineButton
            // 
            this.MineButton.Location = new System.Drawing.Point(12, 418);
            this.MineButton.Name = "MineButton";
            this.MineButton.Size = new System.Drawing.Size(75, 23);
            this.MineButton.TabIndex = 0;
            this.MineButton.Text = "Mine";
            this.MineButton.UseVisualStyleBackColor = true;
            // 
            // ScanButton
            // 
            this.ScanButton.Location = new System.Drawing.Point(93, 418);
            this.ScanButton.Name = "ScanButton";
            this.ScanButton.Size = new System.Drawing.Size(75, 23);
            this.ScanButton.TabIndex = 1;
            this.ScanButton.Text = "Scan";
            this.ScanButton.UseVisualStyleBackColor = true;
            // 
            // TalkButton
            // 
            this.TalkButton.Location = new System.Drawing.Point(174, 418);
            this.TalkButton.Name = "TalkButton";
            this.TalkButton.Size = new System.Drawing.Size(75, 23);
            this.TalkButton.TabIndex = 2;
            this.TalkButton.Text = "Talk";
            this.TalkButton.UseVisualStyleBackColor = true;
            // 
            // AttackButton
            // 
            this.AttackButton.Location = new System.Drawing.Point(255, 418);
            this.AttackButton.Name = "AttackButton";
            this.AttackButton.Size = new System.Drawing.Size(75, 23);
            this.AttackButton.TabIndex = 3;
            this.AttackButton.Text = "Attack";
            this.AttackButton.UseVisualStyleBackColor = true;
            // 
            // ShipBox
            // 
            this.ShipBox.Location = new System.Drawing.Point(336, 12);
            this.ShipBox.Name = "ShipBox";
            this.ShipBox.Size = new System.Drawing.Size(284, 400);
            this.ShipBox.TabIndex = 6;
            this.ShipBox.TabStop = false;
            this.ShipBox.Text = "Ship";
            // 
            // MapBox
            // 
            this.MapBox.Location = new System.Drawing.Point(12, 12);
            this.MapBox.Name = "MapBox";
            this.MapBox.Size = new System.Drawing.Size(318, 236);
            this.MapBox.TabIndex = 7;
            this.MapBox.TabStop = false;
            this.MapBox.Text = "Map";
            // 
            // InfoBox
            // 
            this.InfoBox.Controls.Add(this.InfoText);
            this.InfoBox.Location = new System.Drawing.Point(12, 254);
            this.InfoBox.Name = "InfoBox";
            this.InfoBox.Size = new System.Drawing.Size(318, 158);
            this.InfoBox.TabIndex = 8;
            this.InfoBox.TabStop = false;
            this.InfoBox.Text = "Information";
            // 
            // InfoText
            // 
            this.InfoText.AutoSize = true;
            this.InfoText.Location = new System.Drawing.Point(6, 16);
            this.InfoText.Name = "InfoText";
            this.InfoText.Size = new System.Drawing.Size(75, 13);
            this.InfoText.TabIndex = 0;
            this.InfoText.Text = "Info goes here";
            // 
            // MoveButton
            // 
            this.MoveButton.Location = new System.Drawing.Point(336, 418);
            this.MoveButton.Name = "MoveButton";
            this.MoveButton.Size = new System.Drawing.Size(75, 23);
            this.MoveButton.TabIndex = 9;
            this.MoveButton.Text = "Move To:";
            this.MoveButton.UseVisualStyleBackColor = true;
            // 
            // MoveCoordsInput
            // 
            this.MoveCoordsInput.Location = new System.Drawing.Point(417, 418);
            this.MoveCoordsInput.Name = "MoveCoordsInput";
            this.MoveCoordsInput.Size = new System.Drawing.Size(122, 20);
            this.MoveCoordsInput.TabIndex = 10;
            // 
            // ToMenuButton
            // 
            this.ToMenuButton.Location = new System.Drawing.Point(545, 418);
            this.ToMenuButton.Name = "ToMenuButton";
            this.ToMenuButton.Size = new System.Drawing.Size(75, 23);
            this.ToMenuButton.TabIndex = 11;
            this.ToMenuButton.Text = "To Menu";
            this.ToMenuButton.UseVisualStyleBackColor = true;
            this.ToMenuButton.Click += new System.EventHandler(this.ToMenuButton_Click);
            // 
            // PlanetaryGameForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(632, 453);
            this.Controls.Add(this.ToMenuButton);
            this.Controls.Add(this.MoveCoordsInput);
            this.Controls.Add(this.MoveButton);
            this.Controls.Add(this.InfoBox);
            this.Controls.Add(this.MapBox);
            this.Controls.Add(this.ShipBox);
            this.Controls.Add(this.AttackButton);
            this.Controls.Add(this.TalkButton);
            this.Controls.Add(this.ScanButton);
            this.Controls.Add(this.MineButton);
            this.Name = "PlanetaryGameForm";
            this.Text = "Planetary";
            this.InfoBox.ResumeLayout(false);
            this.InfoBox.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button MineButton;
        private System.Windows.Forms.Button ScanButton;
        private System.Windows.Forms.Button AttackButton;
        private System.Windows.Forms.GroupBox ShipBox;
        private System.Windows.Forms.GroupBox MapBox;
        private System.Windows.Forms.GroupBox InfoBox;
        private System.Windows.Forms.Button MoveButton;
        private System.Windows.Forms.TextBox MoveCoordsInput;
        protected System.Windows.Forms.Button TalkButton;
        private System.Windows.Forms.Label InfoText;
        private System.Windows.Forms.Button ToMenuButton;
    }
}

