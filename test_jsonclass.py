from jsonclass import HumanDict, AttrNotFoundException


d = {
    "task_id": "817593",
    "priority": 8,
    "args": ["slice", "av", "probe"],
    "task_list": [
	{"option_key":"1", "value":"x"},
	{"option_key":"2", "value":"x"},
	{"option_key":"3", "value":"x"},
    ],
    "body": {
        "slice": {
            "bit": "128k",
            "aq": "8k",
            "vq": "16k",
            "extra": {
                "qiniu": "qiniu.com",
                "fastdfs": "/root"
            },
        },
    }
}

if __name__ == "__main__":
    human = HumanDict(d)
    assert human.task_id == d["task_id"]
    assert human.args[0] == d["args"][0]
    assert len(human.task_list) == len(d["task_list"])

    assert human.body.slice.extra.qiniu == "qiniu.com"
    try:
        print human.body.slice.extra.not_found
    except AttrNotFoundException:
        print "catch AttrNotFoundException"
