# Lecture 1 Practice 3
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)
    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            # TODO: Open file
            file = open(filename, 'r', encoding='utf-8')
        except FileNotFoundError:
            # TODO: Handle missing file
            print(f"Error: The file '{filename}' was not found.")
            return None
        except PermissionError:
            # TODO: Handle permission issues
            print(f"Error: Permission denied when trying to access '{filename}'.")
            return None
        else:
            # TODO: Process file content (only if opened successfully)
            content = file.read()
            return content.strip()
        finally:
            # TODO: Ensure file is closed
            if file is not None:
                file.close()
    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")
    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None
        def acquire(self):
            """Acquire resource - might fail."""
            # TODO: Implement with possible RuntimeError
            import random
            if random.random() < 0.2:
                raise RuntimeError(f"Failed to acquire resource: {self.name}")
            self.resource = f"<{self.name} Handle>"
            print(f"Resource '{self.name}' acquired successfully.")
        def release(self):
            """Release resource - must always happen."""
            # TODO: Implement cleanup
            if self.resource:
                print(f"Resource '{self.name}' released/cleaned up.")
                self.resource = None
            else:
                print(f"Resource '{self.name}' was not active or already released.")
        def use(self):
            """Use resource - only if acquired."""
            # TODO: Implement usage
            if not self.resource:
                raise ValueError(f"Cannot use unacquired resource: {self.name}")
            print(f"Using resource: {self.resource}")
    # Test resource management
    rm = ResourceManager("Database")
    # TODO: Use try-except-else-finally to manage resource
    try:
        rm.acquire()
    except RuntimeError as e:
        print(f"Caught an exception during acquisition: {e}")
    else:
        try:
            rm.use()
        except Exception as e:
            print(f"Error during usage: {e}")
    finally:
        rm.release()
# Run the practice
practice_3_complete_pattern()


# Lecture 2 Practice 2
def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)
    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass
    class InvalidMoveError(GameError):
        """Invalid game move."""
        # TODO: Add __init__ with position and reason
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"Move to position {position} is invalid: {reason}")
        pass
    class GameOverError(GameError):
        """Game has ended."""
        # TODO: Add __init__ with winner
        def __init__(self, winner=None):
            self.winner = winner
            msg = f"Winner: {winner}" if winner else "Game ended in a draw/already over."
            super().__init__(msg)
        pass
    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
        def make_move(self, row, col):
            # TODO: Raise GameOverError if game_over is True
            if self.game_over:
                raise GameOverError(winner=None)
            # TODO: Raise InvalidMoveError if position is taken
            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "Square is already occupied.")
            # TODO: Raise InvalidMoveError if position is out of bounds
            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Position out of bounds (must be between 0 and 2).")
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            pass
    # Test the game
    game = TicTacToe()
    test_moves = [
        (0, 0), # Valid
        (0, 0), # Already taken
        (5, 5), # Out of bounds
    ]
    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")
# Run the practice
practice_2_custom_exceptions()


# Lecture 2 Practice 3
def practice_3_complete_system():
    import os
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)
    # TODO: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []
        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            # TODO: Implement with try-except-else-finally
            file = None
            try:
                file = open(filename, 'r', encoding='utf-8')
            # TODO: Handle FileNotFoundError
            except FileNotFoundError:
                print(f"❌ Error: File not found -> '{filename}'")
                self.failed_files.append((filename, "FileNotFoundError"))
                return None
            # TODO: Handle PermissionError
            except PermissionError:
                print(f"❌ Error: Permission denied -> '{filename}'")
                self.failed_files.append((filename, "PermissionError"))
                return None
            # TODO: Handle general exceptions
            except Exception as e:
                print(f"❌ Error: Unexpected issue with '{filename}' -> {e}")
                self.failed_files.append((filename, type(e).__name__))
                return None
            else:
                try:
                    content = file.read()
                    print(f"✅ Successfully processed: '{filename}")
                    self.processed_files.append(filename)
                    return content
                except Exception as read_error:
                    print(f"❌ Error reading content of '{filename}': -> {read_error}")
                    self.failed_files.append((filename, "ReadError"))
                    return None
            # TODO: Ensure file is closed
            finally:
                if file is not None:
                    file.close()
            pass
        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            # TODO: Process each file
            try:
                for filename in os.listdir(directory):
                    filepath = os.path.join(directory, filename)
                    if os.path.isfile(filepath):
                        self.process_file(filepath)
            # TODO: Continue on errors
            except Exception as e:
                print(f"❌ Failed to scan directory '{filename}': {e}")
            pass
        def get_report(self):
            """
            Get processing report.
            """
            # TODO: Return summary of processing
            return {
                "total_successful": len(self.processed_files),
                "total_failed": len(self.failed_files),
                "processed_files": self.processed_files,
                "failed_files": self.failed_files
            }
            pass
    # Test the processor
    processor = FileProcessor()
    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]
    for filename in test_files:
        processor.process_file(filename)
    report = processor.get_report()
    print(f"Report: {report}")
# Run the practice
practice_3_complete_system()