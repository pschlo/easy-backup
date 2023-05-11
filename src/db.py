import yaml


VALID_KEYS = {
    'ID':None,
    'name':None,
    'sources':None,
    'destination':None,
    'intervals':None,

}


class IDError(ValueError):
    def __init__(self, id):
        msg = "Invalid ID '%s'" % id
        super().__init__(msg)


class DB:
    def __init__(self, path):
        self.path = path

    # get specific backup definition by id
    def get(self, id=None, *args):
        if id is None:
            return self._get_all()
        for i in self._get_all():
            if i['ID'] == id:
                # found correct backup definition

                if len(args) == 0:
                    return i
                # get values of keys listed in args
                values = []
                for key in args:
                    if key not in i:
                        raise KeyError(key)
                    else:
                        values.append(i[key])
                # tuple if multiple values, else string
                return tuple(values) if len(values) > 1 else values.pop()

        raise IDError(id)

    # get all backup definitions
    def _get_all(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
    
    def update(self, id, **kwargs):
        data = self._get_all()
        for i in data:
            if i['ID'] == id:
                # replace in i according to kwargs, then write new i
                for key, value in kwargs.items():
                    i[key] = value
                self._write(data)
                return
        raise IDError(id)

    def _write(self, data):
        with open(self.path, 'w', encoding='utf-8') as f:
            # convert data to yml string
            data_dump = yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
            # write beautified yml string to file
            f.write(self._beautify(data_dump))

    
    def _beautify(self, data_dump):
        # beautify the yml dump
        result = ''
        add_spaces = None
        for line in data_dump.split('\n'):
            if len(line) > 0:
                # insert blank line after every backup definition
                if line[0] == '-':
                    result += '\n'
                # quick-and-dirty code to indent the list of sources
                if line.strip().split(':')[0] == 'destination':
                    add_spaces = False
                if add_spaces:
                    result += '  '
                if line.strip().split(':')[0] == 'sources':
                    add_spaces = True
            result += line + '\n'
        # remove redundant last blank line
        result = result[:-1]
        return result
    
    def delete(self, id):
        data = self._get_all()
        for i in data:
            if i['ID'] == id:
                data.remove(i)
                self._write(data)
                return
        raise IDError(id)
        # self._write([i for i in self._get_all() if i['ID'] != id])
    
    def add(self, new_item, id=None):
        data = self._get_all()
        max_id = max([i['ID'] for i in data])
        new_item['ID'] = max_id + 1 if id is None else id
        data.append(new_item)
        self._write(data)


    # print(data)
    # for i in data:
    #     for j in i.items():
    #         print('%s: %s' % j)
    #     print()




db = DB(r'testfolder\test_dump.txt')
# print(db.get(1, 'destination'))
# db.update(1, destination="D:\\")
# print(db.get(5, 'namsdf'))
# db.update(0)
db.add({'name':'test'})
