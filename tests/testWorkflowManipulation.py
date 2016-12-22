import unittest, ast

from core import controller

class TestWorkflowManipulation(unittest.TestCase):
    def setUp(self):
        self.c = controller.Controller()
        self.c.loadWorkflowsFromFile(path="tests/testWorkflows/simpleDataManipulationWorkflow.workflow")
        self.testWorkflow = self.c.workflows["helloWorldWorkflow"]

    def reset(self):
        self.c.loadWorkflowsFromFile(path="tests/testWorkflows/simpleDataManipulationWorkflow.workflow")
        self.testWorkflow = self.c.workflows["helloWorldWorkflow"]

    def executionTest(self):
        # Check that the workflow executed correctly post-manipulation
        steps, instances = self.testWorkflow.execute()
        instances = ast.literal_eval(instances)
        self.assertTrue(len(steps) == 2)
        self.assertTrue(len(instances) == 1)
        self.assertTrue(steps[0].id == "start")
        self.assertTrue(steps[0].output == "REPEATING: Hello World")
        self.assertTrue(steps[1].id == "1")
        self.assertTrue(steps[1].output == "REPEATING: This is a test.")
    """
        CRUD - Workflow
    """
    def test_createWorkflow(self):
        pass

    def test_removeWorkflow(self):
        pass

    def test_updateWorkflow(self):
        pass

    def test_displayWorkflow(self):
        pass

    """
        CRUD - Step
    """
    def test_createStep(self):
        self.testWorkflow.createStep(id="1", action="repeatBackToMe", app="HelloWorld", device="hwTest",
                                     input={"call":{"tag":"call", "value":"This is a test.", "format":"string"}})

        steps = self.testWorkflow.steps

        #Check that the step was added
        self.assertTrue(len(steps) == 2)
        self.assertTrue(steps["1"])

        #Check attributes
        step = self.testWorkflow.steps["1"]
        self.assertTrue(step.id == "1")
        self.assertTrue(step.action == "repeatBackToMe")
        self.assertTrue(step.app == "HelloWorld")
        self.assertTrue(step.device == "hwTest")
        #self.assertTrue(step.input == {'call': {'value': 'This is a test.', 'type': 'string', 'key': 'call'}}))
        self.assertTrue(step.next == [])
        self.assertTrue(step.errors == [])

        self.executionTest()
        self.reset()

    def test_addStepToXML(self):
        self.testWorkflow.createStep(id="1", action="repeatBackToMe", app="HelloWorld", device="hwTest",
                                     input={"call": {"tag": "call", "value": "This is a test.", "format": "string"}})

        xml = self.testWorkflow.toXML()

        #Verify Structure
        steps = xml.findall(".//steps/step")
        self.assertTrue(len(steps) == 2)
        step = xml.find(".//steps/step/[@id='1']")
        self.assertTrue(step.get("id") == "1")
        self.assertTrue(step.find(".//action").text == "repeatBackToMe")
        self.assertTrue(step.find(".//app").text == "HelloWorld")
        self.assertTrue(step.find(".//device").text == "hwTest")
        #self.assertTrue(et.dump(step.find(".//input")) == "<input><call format=\"string\">This is a test.</call></input>")
        self.assertTrue(step.find(".//next") == None)
        self.assertTrue(step.find(".//error") == None)

        self.executionTest()
        self.reset()

    def test_removeStep(self):
        self.testWorkflow.createStep(id="1", action="repeatBackToMe", app="HelloWorld", device="hwTest",
                                     input={"call": {"tag": "call", "value": "This is a test.", "format": "string"}})
        #Makes sure a new step was created...
        self.assertTrue(len(self.testWorkflow.steps) == 2)

        #...So that we may destroy it!
        removed = self.testWorkflow.removeStep(id="1")
        self.assertTrue(removed)
        self.assertTrue(len(self.testWorkflow.steps) == 1)

        #Tests the XML representation after changes
        xml = self.testWorkflow.toXML()
        steps = xml.findall(".//steps/*")
        self.assertTrue(len(steps) == 1)
        self.assertTrue(steps[0].get("id") == "start")
        self.reset()

    def test_updateStep(self):
        self.assertTrue(self.testWorkflow.steps["start"].action == "repeatBackToMe")
        self.testWorkflow.steps["start"].set(attribute="action", value="helloWorld")
        self.assertTrue(self.testWorkflow.steps["start"].action == "helloWorld")

        xml = self.testWorkflow.toXML()
        self.assertTrue(xml.find(".//steps/step/[@id='start']/action").text == "helloWorld")

    def test_displaySteps(self):
        output = ast.literal_eval(self.testWorkflow.__repr__())
        self.assertTrue(output["options"])
        self.assertTrue(output["steps"])
        self.assertTrue(len(output["steps"]) == 1)
        self.assertTrue(output["steps"]["start"]["action"] == "repeatBackToMe")


    """
        CRUD - Flag
    """

    def test_createFlag(self):
        self.assertEqual(True, True)

    def test_removeFlag(self):
        self.assertEqual(True, True)

    def test_updateFlag(self):
        self.assertEqual(True, True)

    def test_displayFlag(self):
        self.assertEqual(True, True)

    """
        CRUD - Filter
    """

    def test_createFilter(self):
        self.assertEqual(True, True)

    def test_removeFilter(self):
        self.assertEqual(True, True)

    def test_updateFilter(self):
        self.assertEqual(True, True)

    def test_displayFilter(self):
        self.assertEqual(True, True)

    """
        CRUD - Options
    """

    def test_createOption(self):
        self.assertEqual(True, True)


    def test_removeOption(self):
        self.assertEqual(True, True)

    def test_updateOption(self):
        self.assertEqual(True, True)

    def test_displayOption(self):
        self.assertEqual(True, True)






