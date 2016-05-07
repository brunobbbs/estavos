var PhoneMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
phoneOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(PhoneMaskBehavior.apply({}, arguments), options);
    }
};
