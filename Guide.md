# Developer Guide – Snake, Water, Gun

## Code Flow

1. **Choices List**: `["snake", "water", "gun"]`  
2. **Winning Logic**: Defined in `win_map`.  
   - Snake > Water  
   - Water > Gun  
   - Gun > Snake  
3. **Gameplay Loop**: Runs for 5 rounds.  
   - Player inputs choice.  
   - AI picks random choice.  
   - Winner is decided via `get_result()`.  
   - Score is updated.  

## Functions

- `get_result(You, AI)` → Returns result of a round.  

## Extensions

- Change `for _ in range(5):` to allow unlimited rounds.  
- Replace `input()` with GUI buttons for better UX.  
- Store results in a `.csv` file for analytics.  