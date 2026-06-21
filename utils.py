def calculate_fps(frame_times):
    if not frame_times:
        return 0
    return len(frame_times) / sum(frame_times)


def limit_fps(max_fps):
    frame_duration = 1.0 / max_fps
    start_time = time.time()

    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - start_time
            if elapsed < frame_duration:
                time.sleep(frame_duration - elapsed)
            start_time = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator


def load_image(path):
    try:
        image = pygame.image.load(path)
        return image
    except pygame.error as e:
        print(f'Error loading image: {e}')
        return None


def save_game_state(state, filename):
    with open(filename, 'w') as f:
        json.dump(state, f)


def load_game_state(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading game state: {e}')
        return None
