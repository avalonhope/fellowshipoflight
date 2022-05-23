def subfaction(child, parent):
    """Check if one faction is a subfaction of another."""
    if child is parent:
        return True
    if child.db.superfaction is None:
        return False
    if child.db.superfaction is parent:
        return True
    subfaction = child.db.superfaction
    found = False
    while subfaction.db.superfaction is not None:
        if subfaction.db.superfaction is parent:
            found = True
            break
        subfaction = subfaction.db.superfaction
    return found
