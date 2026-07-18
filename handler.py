from typing import List, Dict, Any
import random

class GameEvent:
    def __init__(self, event_type: str, details: Dict[str, Any]) -> None:
        self.event_type = event_type
        self.details = details

    def __str__(self) -> str:
        return f"GameEvent(type={self.event_type}, details={self.details})"

def generate_random_event() -> GameEvent:
    event_types: List[str] = ['jump', 'run', 'shoot', 'cast_spell']
    event_type: str = random.choice(event_types)
    details: Dict[str, Any] = {'strength': random.randint(1, 100), 'accuracy': random.uniform(0.1, 1.0)}
    return GameEvent(event_type, details)

def handle_event(event: GameEvent) -> None:
    print(f"Handling event: {event}")
    if event.event_type == 'shoot':
        print(f"Shooting with strength {event.details['strength']} and accuracy {event.details['accuracy']}")
    elif event.event_type == 'jump':
        print("Jumping high!")
    elif event.event_type == 'run':
        print(f"Running with strength {event.details['strength']}")
    elif event.event_type == 'cast_spell':
        print("Casting a powerful spell!")

if __name__ == '__main__':
    for _ in range(5):
        event = generate_random_event()
        handle_event(event)
