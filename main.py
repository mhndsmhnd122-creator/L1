Modify main.py to handle advanced FFmpeg drawtext configurations. 
1. Create a dynamic FFmpeg command builder that takes these inputs from the UI:
   - Text Content (The actual text).
   - Text Color (Hex color picker).
   - Text Size (Numeric input).
   - Text Position (Dropdown: Top-Left, Top-Right, Bottom-Left, Bottom-Right, Center).
   - Font File (A selection for standard fonts available in the system).
2. Ensure the drawtext filter in FFmpeg command is correctly escaped for variables.
3. Add a 'Preview Settings' section in the Flask dashboard to verify the command string before starting the stream.
4. Make sure the 'Stream Key' input field is type="text" to remain visible.
 
