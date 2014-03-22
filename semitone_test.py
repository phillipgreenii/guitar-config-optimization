import unittest
from semitone import Semitone


class SemitoneTest(unittest.TestCase):

  def test_constructor_should_default_sharps_to_zero(self):
    instance = Semitone('D')

    self.assertEqual(instance.sharps,0)
  
  def test_constructor_should_default_flats_to_zero(self):
    instance = Semitone('D')

    self.assertEqual(instance.flats,0)

  def test_constructor_with_uppercase_note_should_work(self):
    instance = Semitone('D',sharps=1,flats=2)

    self.assertIsNotNone(instance)
    self.assertEqual(instance.note,'D')
    self.assertEqual(instance.sharps,1)
    self.assertEqual(instance.flats,2)

  def test_constructor_with_lowercase_note_should_work(self):
    instance = Semitone('d',sharps=1,flats=2)

    self.assertIsNotNone(instance)
    self.assertEqual(instance.note,'D')
    self.assertEqual(instance.sharps,1)
    self.assertEqual(instance.flats,2)

  def test_constructor_with_note_longer_than_1_letter_should_raise_value_error(self):
    self.assertRaises(ValueError,Semitone,'D#')

  def test_constructor_with_invalid_note_should_raise_value_error(self):
    self.assertRaises(ValueError,Semitone,'X') 

  def test_constructor_with_empty_note_should_raise_value_error(self):
    self.assertRaises(ValueError,Semitone,'') 

  def test_constructor_with_no_note_should_raise_value_error(self):
    self.assertRaises(ValueError,Semitone,None) 


  def test_from_string_with_natural_should_create_correct_semiton(self):
    expected_semitone = Semitone('D')
    result = Semitone.from_string('D')

    self.assertSame(result,expected_semitone)

  def test_from_string_with_sharp_should_create_correct_semitone(self):
    expected_semitone = Semitone('D',sharps=2)
    result = Semitone.from_string('D##')
    
    self.assertSame(result,expected_semitone)

  def test_from_string_with_flats_should_create_correct_semitone(self):
    expected_semitone = Semitone('D',flats=2)
    result = Semitone.from_string('Dbb')
    
    self.assertSame(result,expected_semitone)

  def test_from_string_with_sharps_and_flats_should_create_correct_semitone(self):
    expected_semitone = Semitone('D',flats=2,sharps=1)
    result = Semitone.from_string('D#bb')
    
    self.assertSame(result,expected_semitone)

  def test_from_string_with_sharps_and_flats_in_wrong_order_should_raise_value_error(self):
    self.assertRaises(ValueError,Semitone.from_string,('Dbb#',)) 

  def test_from_string_with_garbage_should_raise_value_error(self):
    self.assertRaises(ValueError,Semitone.from_string,('BEAD',)) 

  def test_equals_should_return_true_with_same_instanace(self):
    instance = Semitone('D')

    self.assertEqual(instance,instance)

  def test_equals_should_return_true_with_same_property_values(self):
    instance = Semitone('D')
    equal_semitone = Semitone('D')

    self.assertEqual(instance,equal_semitone)

  def test_equals_should_return_true_with_unnormalized_form_of_semitone(self):
    instance = Semitone('D')
    equal_semitone = Semitone('D',flats=1,sharps=1)

    self.assertEqual(instance,equal_semitone)

  def test_equals_should_return_true_with_different_form_of_same_semitone(self):
    instance = Semitone('D')
    equal_semitone = Semitone('E',flats=2)

    self.assertEqual(instance,equal_semitone)

  def test_equals_should_return_false_with_different_note(self):
    instance = Semitone('D')
    not_equal_semitone = Semitone('E')

    self.assertNotEqual(instance,not_equal_semitone)

  def test_equals_should_return_false_with_different_sharps(self):
    instance = Semitone('D')
    not_equal_semitone = Semitone('D',sharps=1)

    self.assertNotEqual(instance,not_equal_semitone)

  def test_equals_should_return_false_with_different_flats(self):
    instance = Semitone('D')
    not_equal_semitone = Semitone('D',flats=1)

    self.assertNotEqual(instance,not_equal_semitone)

  def test_sharpen_should_sharpen_natural(self):
    expected_semitone = Semitone('D',sharps=1)
    instance = Semitone('D')

    result = instance.sharpen()

    self.assertSame(result,expected_semitone)

  def test_sharpen_should_sharpen_sharp(self):
    expected_semitone = Semitone('D',sharps=2)
    instance = Semitone('D',sharps=1)

    result = instance.sharpen()

    self.assertSame(result,expected_semitone)

  def test_sharpen_should_neutralize_flat(self):
    expected_semitone = Semitone('D')
    instance = Semitone('D',flats=1)

    result = instance.sharpen()

    self.assertSame(result,expected_semitone)

  def test_flatten_should_flatten_natural(self):
    expected_semitone = Semitone('D',flats=1)
    instance = Semitone('D')

    result = instance.flatten()

    self.assertSame(result,expected_semitone)

  def test_flatten_should_flatten_flat(self):
    expected_semitone = Semitone('D',flats=2)
    instance = Semitone('D',flats=1)

    result = instance.flatten()

    self.assertSame(result,expected_semitone)

  def test_flatten_should_neutralize_sharp(self):
    expected_semitone = Semitone('D')
    instance = Semitone('D',sharps=1)

    result = instance.flatten()

    self.assertSame(result,expected_semitone)


  def test_str_should_display_naturals_correctly(self):
    expected_str= 'D'
    instance = Semitone('D')

    result = str(instance)

    self.assertEqual(result,expected_str)

  def test_str_should_display_sharps_correctly(self):
    expected_str= 'D#'
    instance = Semitone('D',sharps=1)

    result = str(instance)

    self.assertEqual(result,expected_str)

  def test_str_should_display_double_sharps_correctly(self):
    expected_str= 'D##'
    instance = Semitone('D',sharps=2)

    result = str(instance)

    self.assertEqual(result,expected_str)

  def test_str_should_display_flats_correctly(self):
    expected_str= 'Db'
    instance = Semitone('D',flats=1)

    result = str(instance)

    self.assertEqual(result,expected_str)

  def test_str_should_display_double_flats_correctly(self):
    expected_str= 'Dbb'
    instance = Semitone('D',flats=2)

    result = str(instance)

    self.assertEqual(result,expected_str)

  def test_str_should_display_not_normalize_display(self):
    expected_str= 'D##bb'
    instance = Semitone('D',sharps=2,flats=2)

    result = str(instance)

    self.assertEqual(result,expected_str)


  def test_normailze_should_do_nothing_to_normalized_natural_semitone(self):
    expected_semitone = Semitone('D')
    instance = Semitone('D')

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_do_nothing_to_normalized_sharp_semitone(self):
    expected_semitone = Semitone('D',sharps=1)
    instance = Semitone('D',sharps=1)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_do_nothing_to_normalized_flat_semitone(self):
    expected_semitone = Semitone('D',flats=1)
    instance = Semitone('D',flats=1)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_reduce_sharps_when_more_than_12(self):
    expected_semitone = Semitone('D',sharps=1)
    instance = Semitone('D',sharps=13)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_reduce_flats_when_more_than_12(self):
    expected_semitone = Semitone('D', flats=1)
    instance = Semitone('D',flats=13)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_normalize_when_both_flats_and_sharps_are_nonzero(self):
    expected_semitone = Semitone('D',sharps=1)
    instance = Semitone('D',flats=1,sharps=2)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_normalize_when_more_than_one_flat(self):
    expected_semitone = Semitone('C')
    instance = Semitone('D',flats=2)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)
 
  def test_normailze_should_normalize_when_more_than_one_sharp(self):
    expected_semitone = Semitone('E')
    instance = Semitone('D',sharps=2)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_normalize_irregular_flat_semitones(self):
    expected_semitone = Semitone('E')
    instance = Semitone('F',flats=1)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_normailze_should_normalize_irregular_sharp_semitones(self):
    expected_semitone = Semitone('C')
    instance = Semitone('B',sharps=1)

    result = instance.normalize()
   
    self.assertSame(result,expected_semitone)

  def test_as_note_with_same_note_should_do_nothing(self):
    expected_semitone = Semitone('D')
    instance = Semitone('D')

    result = instance.as_note('D')

    self.assertSame(result,expected_semitone)

  def test_as_note_with_notes_less_than_3_higher_should_be_sharped_from_natural(self):
    instance = Semitone('D')

    self.assertSame(instance.as_note('C'),Semitone('C',sharps=2))
    self.assertSame(instance.as_note('B'),Semitone('B',sharps=3))
    self.assertSame(instance.as_note('A'),Semitone('A',sharps=5))

  def test_as_note_with_notes_less_than_3_lower_should_be_flattened_from_natural(self):
    instance = Semitone('D')

    self.assertSame(instance.as_note('E'),Semitone('E',flats=2))
    self.assertSame(instance.as_note('F'),Semitone('F',flats=3))
    self.assertSame(instance.as_note('G'),Semitone('G',flats=5))

  def test_as_note_with_notes_less_than_3_higher_should_be_sharped_from_sharp(self):
    instance = Semitone('D',sharps=1)

    self.assertSame(instance.as_note('C'),Semitone('C',sharps=3))
    self.assertSame(instance.as_note('B'),Semitone('B',sharps=4))
    self.assertSame(instance.as_note('A'),Semitone('A',sharps=6))

  def test_as_note_with_notes_less_than_3_lower_should_be_flattened_from_sharp(self):
    instance = Semitone('D',sharps=1)

    self.assertSame(instance.as_note('E'),Semitone('E',flats=1))
    self.assertSame(instance.as_note('F'),Semitone('F',flats=2))
    self.assertSame(instance.as_note('G'),Semitone('G',flats=4))

  def test_as_note_with_notes_less_than_3_higher_should_be_sharped_from_flat(self):
    instance = Semitone('D',flats=1)

    self.assertSame(instance.as_note('C'),Semitone('C',sharps=1))
    self.assertSame(instance.as_note('B'),Semitone('B',sharps=2))
    self.assertSame(instance.as_note('A'),Semitone('A',sharps=4))

  def test_as_note_with_notes_less_than_3_lower_should_be_flattened_from_flat(self):
    instance = Semitone('D',flats=1)

    self.assertSame(instance.as_note('E'),Semitone('E',flats=3))
    self.assertSame(instance.as_note('F'),Semitone('F',flats=4))
    self.assertSame(instance.as_note('G'),Semitone('G',flats=6))

  def test_as_note_with_note_longer_than_1_letter_should_raise_value_error(self):
    instance = Semitone('D')
    self.assertRaises(ValueError,instance.as_note,'D#')

  def test_as_note_with_invalid_note_should_raise_value_error(self):
    instance = Semitone('D')
    self.assertRaises(ValueError,instance.as_note,'X') 

  def test_as_note_with_empty_note_should_raise_value_error(self):
    instance = Semitone('D')
    self.assertRaises(ValueError,instance.as_note,'') 

  def test_as_note_with_no_note_should_raise_value_error(self):
    instance = Semitone('D')
    self.assertRaises(ValueError,instance.as_note,None) 

  def test_sub_with_same_semitone(self):
    instance = Semitone('D')
    expected_result = 0
    result = instance - instance
    self.assertEquals(result, expected_result)
  
  def test_sub_with_flattened_semitone(self):
    instance = Semitone('D')
    expected_result = 1
    result = instance - instance.flatten()
    self.assertEquals(result, expected_result)

  def test_sub_with_sharpened_semitone(self):
    instance = Semitone('D')
    expected_result = -1
    result = instance - instance.sharpen()
    self.assertEquals(result, expected_result)

  def test_sub_with_different_semitone(self):
    instance = Semitone('D')
    different_instance = Semitone('C')
    expected_result = 2
    result = instance - different_instance
    self.assertEquals(result, expected_result)

  def test_sub_with_different_flattened_semitone(self):
    instance = Semitone('D')
    different_instance = Semitone('C').flatten()
    expected_result = 3
    result = instance - different_instance
    self.assertEquals(result, expected_result)

  def test_sub_with_different_sharpened_semitone(self):
    instance = Semitone('D')
    different_instance = Semitone('C').sharpen()
    expected_result = 1
    result = instance - different_instance
    self.assertEquals(result, expected_result)


  def test_is_natural_should_return_true_when_equal_number_of_flats_and_sharps(self):
    instance = Semitone('D',sharps=1,flats=1)

    self.assertTrue(instance.is_natural)

  def test_is_natural_should_return_true_when_no_flats_and_no_sharps(self):
    instance = Semitone('D')

    self.assertTrue(instance.is_natural)

  def test_is_natural_should_return_false_when_more_flats_than_sharps(self):
    instance = Semitone('D',flats = 1)

    self.assertFalse(instance.is_natural)

  def test_is_natural_should_return_false_when_more_sharps_than_flats(self):
    instance = Semitone('D',sharps = 1)

    self.assertFalse(instance.is_natural)

  def test_is_flat_should_return_true_when_more_flats_than_sharps(self):
    instance = Semitone('D',flats = 1)

    self.assertTrue(instance.is_flat)

  def test_is_flat_should_return_false_when_no_sharps_or_flats(self):
    instance = Semitone('D')

    self.assertFalse(instance.is_flat)

  def test_is_flat_should_return_false_when_equal_number_of_flats_and_sharps(self):
    instance = Semitone('D', sharps=1, flats=1)

    self.assertFalse(instance.is_flat)

  def test_is_flat_should_return_false_when_more_sharps_than_flats(self):
    instance = Semitone('D', sharps = 1)

    self.assertFalse(instance.is_flat)

  def test_is_sharp_should_return_true_when_more_flats_than_sharps(self):
    instance = Semitone('D', sharps = 1)

    self.assertTrue(instance.is_sharp)

  def test_is_sharp_should_return_false_when_no_sharps_or_flats(self):
    instance = Semitone('D')

    self.assertFalse(instance.is_sharp)

  def test_is_sharp_should_return_false_when_equal_number_of_flats_and_sharps(self):
    instance = Semitone('D', sharps=1, flats=1)

    self.assertFalse(instance.is_sharp)

  def test_is_sharp_should_return_false_when_more_flats_than_sharps(self):
    instance = Semitone('D', flats = 1)

    self.assertFalse(instance.is_sharp)

  def assertSame(self,seminote1,seminote2):
    if(not seminote1.is_same(seminote2)):
      raise AssertionError('%s not the same as %s' % (seminote1,seminote2))

  def assertNotSame(seminote1,seminote2):
    if(seminote1.is_same(seminote2)):
      raise AssertionError('%s the same as %s' % (seminote1,seminote2))

if __name__ == '__main__':
    unittest.main()