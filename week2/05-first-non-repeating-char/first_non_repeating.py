# def first_non_repeating(s, case_sensitive=True):
#     if not s:
#         return None

#     checked_chr = {}
#     if not case_sensitive:
#         s = s.lower()
#     for chr in s:
#         if s.count(chr) != 1:
#             if chr not in checked_chr:
#                 checked_chr[chr] = "checked"
#             else:
#                 continue
#         else:
#             return chr
#     return None


def first_non_repeating(s, case_sensitive=True):
    if not s:
        return None
    if not case_sensitive:
        s = s.lower()
    result = list(filter(lambda chr: s.count(chr) == 1, s))
    return result[0] if result else None
