import re

COMMON_KEYWORDS = [
    "docker", "kubernetes", "jenkins", "git", "github",
    "aws", "ec2", "s3", "iam",
    "ansible", "linux", "ci/cd", "openshift",
    "prometheus", "elk", "cloudwatch"
]

def extract_keywords(jd_text):
    jd_text = jd_text.lower()
    found = []

    for kw in COMMON_KEYWORDS:
        if re.search(rf"\b{kw}\b", jd_text):
            found.append(kw)

    return found

def ats_score(found, total=len(COMMON_KEYWORDS)):
    return round((len(found) / total) * 100, 2)


