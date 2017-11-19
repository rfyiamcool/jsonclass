# jsonclass

对于结构层次深的dict友好访问.

```
from jsonclass import HumanDict


d = {
    "task_id": "817593",
    "priority": 8,
    "args": ["slice", "av", "probe"],
    "task_list": [
		{"option_key":"1", "value":"x"},
		{"option_key":"2", "value":"x"},
		{"option_key":"3", "value":"x"},
    ]
}

if __name__ == "__main__":
    human = HumanDict(d)
    assert human.task_id == d["task_id"]
    assert human.args[0] == d["args"][0]
    assert len(human.task_list) == len(d["task_list"])
```

