import dis

DEBUG = True

if DEBUG:
    def registry_event(event):
        print(f"[DEBUG.ON] {event}")
else:
    def registry_event(event):
        pass

registry_event("User Authenticated")

def simple_sum(a: int, b: float) -> float:
    return a + b


dis.dis(simple_sum)
